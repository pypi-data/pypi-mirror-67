# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gitlab_time_report']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'gitlab-time-report',
    'version': '0.1.dev1',
    'description': '',
    'long_description': None,
    'author': 'Johannes Wildermuth',
    'author_email': 'johannes.wildermuth@hsr.ch',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
