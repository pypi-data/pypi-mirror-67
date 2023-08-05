# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gpr_complex']

package_data = \
{'': ['*']}

install_requires = \
['bokeh', 'numpy', 'scipy']

setup_kwargs = {
    'name': 'gpr-complex',
    'version': '0.3.1',
    'description': 'A GPR library that can work with complex numbers',
    'long_description': '\n[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)\n\nA Gaussian Process Regression (GPR) library that can work with complex numbers.\n\n# Development\n\nFor dependency management and publishing to [Pypi](https://pypi.org/) we use\n[poetry](https://python-poetry.org/).\n\nIf you want to extend `gpr_complex`, clone it from the\n[git repository](https://github.com/darcamo/gpr_complex), run\n`poetry install` to create the virtual environment with the required\ndependencies and run `pre-commit install` to install the commit hooks.\n',
    'author': 'Darlan Cavalcante Moreira',
    'author_email': 'darcamo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/darcamo/gpr_complex',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
