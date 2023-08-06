# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['app_store_connect_client']

package_data = \
{'': ['*'], 'app_store_connect_client': ['jsonschema/*']}

install_requires = \
['black>=19.10b0,<20.0',
 'jsonschema>=3.2.0,<4.0.0',
 'python-dateutil>=2.8.1,<3.0.0',
 'python-dotenv>=0.13.0,<0.14.0',
 'requests>=2.23.0,<3.0.0']

setup_kwargs = {
    'name': 'app-store-connect-client',
    'version': '2.0.1',
    'description': 'Python package for App Store connect Analytics.',
    'long_description': None,
    'author': 'shmokmt',
    'author_email': 'shoma.okamoto@fuller.co.jp',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/shmokmt',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
