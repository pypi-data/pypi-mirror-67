# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['comi']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.1,<8.0.0', 'diskcache>=4.1.0,<5.0.0', 'requests>=2.23.0,<3.0.0']

entry_points = \
{'console_scripts': ['comi = comi.main:main']}

setup_kwargs = {
    'name': 'comi',
    'version': '0.1.1',
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
