# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

modules = \
['gitlab_trigger_helper']
entry_points = \
{'console_scripts': ['APPLICATION-NAME = gitlab-helper']}

setup_kwargs = {
    'name': 'gitlab-trigger-helper',
    'version': '0.1.0',
    'description': '',
    'long_description': None,
    'author': 'Fabio Lima',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'py_modules': modules,
    'entry_points': entry_points,
    'python_requires': '>=2.7,<3.0',
}


setup(**setup_kwargs)
