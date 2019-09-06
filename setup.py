# -*- coding=utf-8 -*-


from setuptools import setup, find_packages


setup(
    name="bulk_geocoding",
    version="0.1.1",
    description="Python client for geocoding adresses in bulk using adresse.data.gouv.fr API",
    author="Benoît Guigal",
    author_email="benoit.guigal@protonmail.com",
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
    python_requires=">=3.6",
    install_requires=['requests'],
    url='https://github.com/MTES-MCT/bulk-geocoding-python-client',
    download_url='https://github.com/MTES-MCT/bulk-geocoding-python-client/archive/v0.1.1.tar.gz',
)