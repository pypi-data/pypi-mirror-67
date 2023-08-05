# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyzoom']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=19.3.0,<20.0.0',
 'pyjwt>=1.7.1,<2.0.0',
 'requests>=2.23.0,<3.0.0',
 'typing-extensions>=3.7.4,<4.0.0']

setup_kwargs = {
    'name': 'pyzoom',
    'version': '0.1.1',
    'description': 'Python wrapper for Zoom Video API',
    'long_description': '# Python wrapper for Zoom API\n',
    'author': 'MB',
    'author_email': 'mb@blaster.ai',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/licht1stein/pyzoom',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
