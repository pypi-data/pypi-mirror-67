# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pandas_cacher']

package_data = \
{'': ['*']}

install_requires = \
['numpy', 'pandas', 'tables']

setup_kwargs = {
    'name': 'pandas-cacher',
    'version': '0.1.2',
    'description': 'Pandas cacher',
    'long_description': None,
    'author': 'Statnett Datascience',
    'author_email': 'Datascience.Drift@statnett.no',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
