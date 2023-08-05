# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyphysim',
 'pyphysim.c_extensions',
 'pyphysim.cell',
 'pyphysim.channel_estimation',
 'pyphysim.channels',
 'pyphysim.comm',
 'pyphysim.extra',
 'pyphysim.extra.MATLAB',
 'pyphysim.ia',
 'pyphysim.mimo',
 'pyphysim.modulators',
 'pyphysim.reference_signals',
 'pyphysim.simulations',
 'pyphysim.subspace',
 'pyphysim.util']

package_data = \
{'': ['*']}

install_requires = \
['configobj', 'matplotlib', 'numba>=0.48.0,<0.49.0', 'numpy', 'scipy']

setup_kwargs = {
    'name': 'pyphysim',
    'version': '0.4',
    'description': 'Implementation of a digital communication (physical layer) in python',
    'long_description': '![Testing](https://travis-ci.org/darcamo/pyphysim.svg?branch=master)\n[![Coverage Status](https://coveralls.io/repos/github/darcamo/pyphysim/badge.svg?branch=master)](https://coveralls.io/github/darcamo/pyphysim?branch=master)\n[![Documentation Status](https://readthedocs.org/projects/pyphysim/badge/?version=latest)](http://pyphysim.readthedocs.io/en/latest/?badge=latest)\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)\n\nPyPhysim\n========\n\nSimulation of Digital Communication (physical layer) in Python.\n\nThis includes classes related to digital modulation, AWGN channels, MIMO,\nOFDM, etc.. It also includes classes related to multiuser transmission such\nas block diagonalization, interference alignment, etc.\n\nFurthermore, a framework for implementing Monte Carlo simulations is also\nimplemented (see the pyphysim.simulations package).\n\n\nNote\n----\n\nInstall [poetry](https://python-poetry.org/), clone this repository and then use\nthe command `poetry install` to install pyphysim.\n\nYou can also directly install it from pypi with `pip install pyphysim`.\n',
    'author': 'Darlan Cavalcante Moreira',
    'author_email': 'darcamo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/darcamo/pyphysim',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
