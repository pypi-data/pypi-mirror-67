# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'source'}

packages = \
['rolodex']

package_data = \
{'': ['*']}

install_requires = \
['colorama>=0.4.3,<0.5.0',
 'pydantic>=1.5,<2.0',
 'pyyaml>=5.3.1,<6.0.0',
 'structlog>=20.1.0,<21.0.0',
 'typer>=0.1.1,<0.2.0']

entry_points = \
{'console_scripts': ['rolodex = rolodex.cli:app'],
 'rolodex.readers': ['json = rolodex.io:JSONReader',
                     'yaml = rolodex.io:YAMLReader'],
 'rolodex.storage': ['json = rolodex.store:JSONStore'],
 'rolodex.writers': ['json = rolodex.io:JSONWriter',
                     'yaml = rolodex.io:YAMLWriter']}

setup_kwargs = {
    'name': 'my-rolodex',
    'version': '0.1.1',
    'description': 'Animal Logic: Technical Challenge',
    'long_description': "[![CircleCI](https://circleci.com/gh/ylathouris/bio.svg?style=shield)](https://circleci.com/gh/ylathouris/rolodex)  ![Coverage](coverage.svg)\n\n---\n\n# Rolodex\n\nThis is my submission for Animal Logic's technical challenge. It is a\nsimple application for managing people's contacts and addresses.\nBefore getting started, let's go over the requirements:\n\n<br/>\n\n### The Requirements\n\n**1:**\n> Create a repository on one of the major development platforms\n> (i.e GitHub, Bitbucket)_\n\n**2:**\n> Provide a CI setup that clones the repository and runs the\n> tests of your code every time code is committed (in any branch).\n\n**3:**\n> Write a command-line tool in python that takes some sets\n> of personal data (name, address, phone number) and serialise\n> them/deserialise them in at least 2 formats, and also display the\n> data it in at least 2 different ways.\n>\n>  * \u200bThere is no need to use a GUI Framework - text output/HTML or\n>    any other human-readable format is fine.\n>\n>  * There is no need to support manual data entry - you could provide\n>    a file in one of your chosen formats to use as input test data.\n>\n>  * Write it in such a way that it would be easy for a developer to:\n>    * add support for additional storage formats.\n>    * query a list of currently supported formats.\n>    * supply an alternative reader/writer for one of the supported\n>      formats.\u200b\n\n\n<br/>\n\n## Next Steps\n\n* [Installation](docs/installation.md)\n* [Concepts](docs/concepts.md)\n* [CLI](docs/cli.md)\n* [API](docs/api.md)\n* [Plugins](docs/plugins.md)\n\n\n\n<br/>\n",
    'author': 'Yani Lathouris',
    'author_email': 'ylathouris@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ylathouris/rolodex',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
