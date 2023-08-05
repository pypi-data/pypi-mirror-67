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
    'version': '0.1.4',
    'description': 'A small CLI utility to monitor bbb usage',
    'long_description': '# bbbmon\n\nA small python based CLI utility to monitor BigBlueButton-Usage. \n\n## Installation\n\nThe easiest way to install bbbmon is to install it from the Python Package Index (PyPi). This project uses [python poetry](https://python-poetry.org/) for dependency management, so you could also run it without installing the package system wide, see instructions below.\n\n## Install with pip3\n\n```bash\nsudo pip3 install bbbmon --upgrade\n```\n\nThen run with:\n\n```bash\nbbbmon\n```\n\n## Run with poetry (without pip)\n\nClone the repo:\n\n```bash\ngit clone https://code.hfbk.net/bbb/bbbmon.git\n```\n\nMake sure you have poetry installed. Install instruction for poetry can be [found here](https://python-poetry.org/docs/#installation).\nFrom inside the project directory run:\n\n```bash\npoetry install\n```\n\nRun bbbmon with:\n\n```bash\npoetry run bbbmon\n```\n\nFor bbbmon to run you need to have a `bbbmon.properties` file at the path specified. In this file there should be your servers secret and the server URL. You can find this secret on your server in the file `/usr/share/bbb-web/WEB-INF/classes/bigbluebutton.properties` (look for a line starting with `securitySalt=` and copy it to). If in doubt just follow the instructions the CLI gives you.\n\n',
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
