# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['gitlab_trigger_helper']
entry_points = \
{'console_scripts': ['APPLICATION-NAME = gilab_trigger_helper:__main__']}

setup_kwargs = {
    'name': 'gitlab-trigger-helper',
    'version': '0.1.1.1',
    'description': '',
    'long_description': None,
    'author': 'Fabio Lima',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'entry_points': entry_points,
    'python_requires': '>=2.7,<3.0',
}


setup(**setup_kwargs)
