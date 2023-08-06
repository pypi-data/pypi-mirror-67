# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

# Avoids IDE errors, but actual version is read from version.py
__version__ = None
exec(open('mingdongtextsim/version.py').read())

if sys.version_info < (3,):
    sys.exit('Sorry, Python3 is required.')

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

with open('LICENSE', 'r', encoding='utf-8') as f:
    license = f.read()

with open('requirements.txt', 'r', encoding='utf-8') as f:
    reqs = f.read()

setup(
    name='mingdongtextsim',
    version=__version__,
    description='Text to vector Tool, encode text',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='',
    author_email='',
    url='',
    license="Apache 2.0",
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',
    ],
    keywords='word embedding,mingdongtextsim,Chinese Text Similarity Calculation Tool,similarity,word2vec',
    install_requires=reqs.strip().split('\n'),
    packages=find_packages(exclude=['tests']),
    package_dir={'mingdongtextsim': 'mingdongtextsim'},
    package_data={
        'mingdongtextsim': ['*.*', 'LICENSE', '../LICENSE', 'README.*', '../*.txt', 'embeddings/*',
                     'utils/*', 'processors/*', 'bert/*'],
    }
)
