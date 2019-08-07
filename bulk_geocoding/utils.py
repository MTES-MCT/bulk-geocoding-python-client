# -*- coding=utf-8 -*-

import csv
from io import StringIO


def csv2dicts(filelike, **kwargs):
    """ transform a csv-like text to an array of dicts records """
    reader = csv.DictReader(filelike, **kwargs)
    return list([dict(row) for row in reader])


def dicts2csv(dicts, **kwargs):
    """ transform an array of dicts to a csv-like text """
    filelike = StringIO()
    fieldnames = list(dicts[0].keys())
    writer = csv.DictWriter(filelike, fieldnames=fieldnames, **kwargs)
    writer.writeheader()
    for record in dicts:
        writer.writerow(record)
    filelike.seek(0)
    return filelike