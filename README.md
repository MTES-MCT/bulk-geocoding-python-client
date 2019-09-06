# bulk-geocoding-python-client

Python client for geocoding adresses in bulk using adresse.data.gouv.fr API

See [https://adresse.data.gouv.fr/api/](https://adresse.data.gouv.fr/api)

This client uses the endpoint `/search/csv`

## Installation

```
pip install bulk-geocoding
```

## Usage

```python

from bulk_geocoding import geocode

adresses = [
  {"numero": "4", "type_voie": "boulevard", "nom_voie": "Longchamp", "numero_insee": "13201"},
  {"numero": "9", "type_voie": "rue", "nom_voie": "des chaufourniers", "numero_insee": "75119"}
]

geocoded = geocode(
  data=adresses,
  columns=["numero", "type_voie", "nom_voie"],
  citycode="numero_insee"
)

print(geocoded)

[
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
```

### Large files

For large files (> 1000 rows) you will need to cut your data into chunks

```python
from bulk_geocoding import geocode

def chunks(l, n):
    """ Yield successive n-sized chunks from l. """
    for i in range(0, len(l), n):
        yield l[i:i + n]


geocoded = []
# split data in chunks
chunk_size = 500
for chunk in chunks(data, chunk_size):
  r = geocode(chunk)
  geocoded += r
```

## Run the tests

* Create a virtualenv and install dependencies

```
pip install -r requirements.txt
```

* Run the tests

```
python -m unittest
```