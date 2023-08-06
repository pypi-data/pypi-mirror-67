# Copyright (c) 2020 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.

import json

from setuptools import setup, find_packages


# Package dependencies
requires = [
    'requests'
]
test_requires = [
    'tox'
]

with open('README.md', encoding='utf-8') as f:
    readme = f.read()

with open('LICENSE') as f:
    license_content = f.read()

with open('version.json') as f:
    info = json.load(f)

setup(
    name='justice-augment-python-sdk',
    version=info['version'],
    description='Python SDK for Justice Augment',
    long_description=readme,
    long_description_content_type='text/markdown; variant=GFM',
    author='Bahrunnur',
    author_email='bahrunnur@accelbyte.io',
    url='https://bitbucket.org/accelbyte/justice-augment-python-sdk',
    license="Copyright (c) 2020 AccelByte Inc.",
    packages=['justice'],
    install_requires=requires,
    tests_require=test_requires,
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
)

