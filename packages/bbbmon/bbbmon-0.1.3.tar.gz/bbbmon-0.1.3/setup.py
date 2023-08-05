# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bbbmon']

package_data = \
{'': ['*']}

install_requires = \
['appdirs>=1.4.3,<2.0.0', 'requests>=2.23.0,<3.0.0']

entry_points = \
{'console_scripts': ['bbbmon = bbbmon.bbbmon:main']}

setup_kwargs = {
    'name': 'bbbmon',
    'version': '0.1.3',
    'description': 'A small CLI utility to monitor bbb usage',
    'long_description': None,
    'author': 'David Huss',
    'author_email': 'david.huss@hfbk-hamburg.de',
    'maintainer': 'David Huss',
    'maintainer_email': 'david.huss@hfbk-hamburg.de',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
