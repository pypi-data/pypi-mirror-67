# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['calamus']

package_data = \
{'': ['*']}

install_requires = \
['marshmallow>=3.5.1,<4.0.0']

setup_kwargs = {
    'name': 'calamus',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Panaetius',
    'author_email': 'ralf.grubenmann@sdsc.ethz.ch',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
