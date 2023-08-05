# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['poetry_deps_formatter']

package_data = \
{'': ['*']}

install_requires = \
['toml>=0.10.0,<0.11.0']

entry_points = \
{'console_scripts': ['format = poetry_deps_formatter:formatter']}

setup_kwargs = {
    'name': 'poetry-deps-formatter',
    'version': '0.1.0',
    'description': 'Beautify dependencies in pyproject.yaml based on poetry.lock',
    'long_description': None,
    'author': 'Jack Klimov',
    'author_email': 'jaklimoff@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
