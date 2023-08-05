# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_githooks']

package_data = \
{'': ['*']}

entry_points = \
{u'poetry_githooks': ['main = poetry_githooks:__main__:main']}

setup_kwargs = {
    'name': 'poetry-githooks',
    'version': '0.1.2',
    'description': '',
    'long_description': None,
    'author': 'Thomas Thiebaud',
    'author_email': 'thiebaud.tom@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
