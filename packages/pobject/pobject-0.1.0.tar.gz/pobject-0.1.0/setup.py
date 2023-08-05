# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pobject']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pobject',
    'version': '0.1.0',
    'description': '',
    'long_description': '# pobject\n',
    'author': 'Eyal Levin',
    'author_email': 'eyalev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
