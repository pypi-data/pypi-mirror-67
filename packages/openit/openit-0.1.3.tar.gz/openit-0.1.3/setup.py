# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['openit']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.2,<8.0.0', 'pobject>=0.1.1,<0.2.0', 'pyyaml>=5.3.1,<6.0.0']

entry_points = \
{'console_scripts': ['o = openit.main:main']}

setup_kwargs = {
    'name': 'openit',
    'version': '0.1.3',
    'description': '',
    'long_description': None,
    'author': 'Eyal Levin',
    'author_email': 'eyalev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
