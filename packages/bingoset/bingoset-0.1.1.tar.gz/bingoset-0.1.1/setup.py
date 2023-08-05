# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bingoset', 'bingoset.utilities']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=7.1.2,<8.0.0', 'requests>=2.23.0,<3.0.0', 'typer[all]>=0.1.1,<0.2.0']

entry_points = \
{'console_scripts': ['bingoset = bingoset.main:app']}

setup_kwargs = {
    'name': 'bingoset',
    'version': '0.1.1',
    'description': '',
    'long_description': '<h4 align="center">\n    <a href="https://github.com/Akshay090/bingoset">\n        <img src="https://raw.githubusercontent.com/Akshay090/bingoset/master/.github/bingoset-banner.png" alt="bingoset" />\n    </a>\n    <br>\n    <br>\n     CLI Toolkit to quickly create image dataset using Bing Image Search API\n\n![Twitter Follow](https://img.shields.io/twitter/follow/aks2899?style=social)\n</h4>\n\n# Welcome to BingoSet \n\n\n## Install\n\n```sh\npip3 install bingoset\n```\n## Set-up\n\nGet your Bingo Image Search API key and execute below command\n\n```sh\nbingoset set-api-key YOUR_BING_API_KEY_HERE\n```\n\n## Usage \n\n```sh\nbingoset q pikachu\n```\nThis will download 250 (default) images of pikachu into a directory called dataset (default)\n\n## Additional Config\n\n```sh\nbingoset set-max-results 100\n```\nChange the number of images you want to download, eg : 100\n\n```sh\nbingoset set-group-size 20\n```\nChange the group size of images you want to download, eg : 100\n',
    'author': 'Akshay Ashok',
    'author_email': 'aks28id@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Akshay090/bingoset',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
