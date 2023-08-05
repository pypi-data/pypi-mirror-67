# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyzoom']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyzoom',
    'version': '0.1.0',
    'description': 'Python wrapper for Zoom Video API',
    'long_description': None,
    'author': 'Mikhail Beliansky',
    'author_email': 'mb@blaster.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
