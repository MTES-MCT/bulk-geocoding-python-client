# -*- coding=utf-8 -*-

import textwrap
from unittest import TestCase, mock

from requests.exceptions import HTTPError

from .bulk_geocoding import geocode


adresses = [
    {
        "numero": "4",
        "type_voie": "boulevard",
        "nom_voie": "Longchamp",
        "numero_insee": "13201"
    },
    {
        "numero": "9",
        "type_voie": "rue",
        "nom_voie": "des chaufourniers",
        "numero_insee": "75119"
    }
]


class BulkGeocodingTestCase(TestCase):

    @mock.patch("bulk_geocoding.bulk_geocoding.requests")
    def test_geocode(self, mock_request):

        mock_response = mock.Mock()
        mock_request.post.return_value = mock_response
        mock_response.status_code = 200
        mock_response.text = """numero,type_voie,nom_voie,numero_insee,latitude,longitude,result_label,result_score,result_type,result_id,result_housenumber,result_name,result_street,result_postcode,result_city,result_context,result_citycode,result_oldcitycode,result_oldcity,result_district
4,boulevard,Longchamp,13201,43.300746,5.387141,4 Boulevard Longchamp 13001 Marseille,0.97,housenumber,13201_5348_00004,4,Boulevard Longchamp,,13001,Marseille,"13, Bouches-du-Rhône, Provence-Alpes-Côte d'Azur",13201,,,Marseille 1er Arrondissement
9,rue,des chaufourniers,75119,48.878693,2.37216,9 Rue des Chaufourniers 75019 Paris,0.98,housenumber,75119_1943_00009,9,Rue des Chaufourniers,,75019,Paris,"75, Paris, Île-de-France",75119,,,Paris 19e Arrondissement
"""

        adresses = [
            {
                "numero": "4",
                "type_voie": "boulevard",
                "nom_voie": "Longchamp",
                "numero_insee": "13201"
            },
            {
                "numero": "9",
                "type_voie": "rue",
                "nom_voie": "des chaufourniers",
                "numero_insee": "75119"
            }
        ]

        geocoded = geocode(
            adresses,
            columns=["numero", "type_voie", "nom_voie"],
            citycode="numero_insee")

        expected = [
            {
                'numero': '4',
                'type_voie': 'boulevard',
                'nom_voie': 'Longchamp',
                'numero_insee': '13201',
                'latitude': '43.300746',
                'longitude': '5.387141',
                'result_label': '4 Boulevard Longchamp 13001 Marseille',
                'result_score': '0.97',
                'result_type': 'housenumber',
                'result_id': '13201_5348_00004',
                'result_housenumber': '4',
                'result_name': 'Boulevard Longchamp',
                'result_street': '',
                'result_postcode': '13001',
                'result_city': 'Marseille',
                'result_context': "13, Bouches-du-Rhône, Provence-Alpes-Côte d'Azur",
                'result_citycode': '13201',
                'result_oldcitycode': '',
                'result_oldcity': '',
                'result_district': 'Marseille 1er Arrondissement'
            }, {
                'numero': '9',
                'type_voie': 'rue',
                'nom_voie': 'des chaufourniers',
                'numero_insee': '75119',
                'latitude': '48.878693',
                'longitude': '2.37216',
                'result_label': '9 Rue des Chaufourniers 75019 Paris',
                'result_score': '0.98',
                'result_type': 'housenumber',
                'result_id': '75119_1943_00009',
                'result_housenumber': '9',
                'result_name': 'Rue des Chaufourniers',
                'result_street': '',
                'result_postcode': '75019',
                'result_city': 'Paris',
                'result_context': '75, Paris, Île-de-France',
                'result_citycode': '75119',
                'result_oldcitycode': '',
                'result_oldcity': '',
                'result_district': 'Paris 19e Arrondissement'
            }
        ]

        self.assertEqual(geocoded, expected)

    @mock.patch("bulk_geocoding.bulk_geocoding.requests")
    def test_geocode_raise_error(self, mock_request):
        """ it should raise an exception if status_code != 200 """

        mock_response = mock.Mock()
        mock_request.post.return_value = mock_response

        error = HTTPError("400 Client Error: BAD REQUEST", response=self)
        mock_response.raise_for_status.side_effect = error

        adresses = [
            {
                "numero": "4",
                "type_voie": "boulevard",
                "nom_voie": "Longchamp",
                "numero_insee": "13201"
            },
            {
                "numero": "9",
                "type_voie": "rue",
                "nom_voie": "des chaufourniers",
                "numero_insee": ""
            }
        ]

        with self.assertRaises(HTTPError) as context:

            geocoded = geocode(
                adresses,
                columns=["numero", "type_voie", "nom_voie"],
                citycode="numero_insee")

