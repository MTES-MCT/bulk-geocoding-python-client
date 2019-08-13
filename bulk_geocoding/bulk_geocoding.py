# -*- coding=utf-8 -*-

import asyncio
from io import StringIO

import requests

from .utils import csv2dicts, dicts2csv


addok_bano_search_csv = 'https://api-adresse.data.gouv.fr/search/csv/'


def geocode(data, columns, citycode=None, postcode=None):
    """
    geocode a in bulk using the /search/csv endpoint
    """

    csvfile = dicts2csv(data, dialect='unix')
    response = geocode_csv(csvfile,
                           columns,
                           citycode=citycode,
                           postcode=postcode)

    return csv2dicts(
        StringIO(response.text),
        dialect='unix')


def geocode_csv(csvlike, columns, citycode=None, postcode=None):

    payload = {'columns': columns}

    if citycode:
        payload['citycode'] = citycode
    if postcode:
        payload['postcode'] = postcode

    files = {'data': csvlike}

    response = requests.post(addok_bano_search_csv, data=payload, files=files)

    response.raise_for_status()

    return response

