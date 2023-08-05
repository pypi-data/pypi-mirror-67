# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fivem']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp', 'toml>=0.10.0,<0.11.0']

setup_kwargs = {
    'name': 'async-fivem',
    'version': '1.0.0',
    'description': 'Async API for FiveM endpoints',
    'long_description': None,
    'author': 'makubob',
    'author_email': 'makupi@icloud.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
