# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gitlab_time_report']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'gitlab-time-report',
    'version': '0.1.dev2',
    'description': 'GitLab time reporting made easy.',
    'long_description': '# GitLab-Timetracking\n\nPlease visit the [Read the Docs](http://ifs.pages.ifs.hsr.ch/gitlab-time-report/gitlab-timetracking/) documentation for more information.\n\n## Development\n\nPlease visit the [according documentation page](http://ifs.pages.ifs.hsr.ch/gitlab-time-report/gitlab-timetracking/development/).\n',
    'author': 'Johannes Wildermuth',
    'author_email': 'johannes.wildermuth@hsr.ch',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://gitlab.dev.ifs.hsr.ch/ifs/gitlab-time-report/gitlab-timetracking',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
