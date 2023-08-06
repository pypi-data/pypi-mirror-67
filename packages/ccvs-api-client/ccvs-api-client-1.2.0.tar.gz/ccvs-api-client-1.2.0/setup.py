# Copyright 2019 WHG (International) Limited. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
import json

from setuptools import find_packages
from setuptools import setup

NAME = 'ccvs-api-client'
VERSION = '1.2.0'

install_requires = []
tests_require = []

with open('Pipfile.lock') as fd:
    lock_data = json.load(fd)
    install_requires = [
        package_name + package_data['version']
        for package_name, package_data in lock_data['default'].items()
    ]
    tests_require = [
        package_name + package_data['version']
        for package_name, package_data in lock_data['develop'].items()
    ]

setup(
    name=NAME,
    version=VERSION,
    description='CCVS API Client',
    author='Ederson Brilhante',
    author_email='ederson.brilhante@grandparade.co.uk',
    url='https://github.com/William-Hill-Online/CCVS-API-Client',
    keywords=['CCVS API'],
    install_requires=install_requires,
    tests_require=tests_require,
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'ccvs-api-scanner=ccvs_scanning_api_client.command.run:main'],
    },
    long_description="""\
        Client for Central Container Vulnerability Scanning API
    """
)
