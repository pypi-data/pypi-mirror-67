# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['vanguardkit']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.9.0,<5.0.0', 'html5lib>=1.0.1,<2.0.0', 'zss>=1.2.0,<2.0.0']

setup_kwargs = {
    'name': 'vanguardkit',
    'version': '0.2.0',
    'description': 'A convenient way to calculate the edit distance between html files',
    'long_description': 'Vanguard kit\n==========================\n\n[![PyPI version](https://badge.fury.io/py/vanguardkit.svg)](https://badge.fury.io/py/vanguardkit)\n[![Tests](https://github.com/BentoBox-Project/vanguard-kit/workflows/CI/badge.svg)](https://github.com/BentoBox-Project/vanguard-kit/actions?workflow=CI)\n[![Codecov](https://codecov.io/gh/BentoBox-Project/vanguard-kit/branch/master/graph/badge.svg)](https://codecov.io/gh/BentoBox-Project/vanguard-kit)\n\n\n> A convenient way to calculate the edit distance between html files to scrape with confidence\n\nSometimes, scraping becomes a hard task, because the web sites are in continous changing.\nWhat about if there was a way to prevent those changes before scrape a site?\nVanguard is a tool kit that provides a way to calculate the edit distance between\ntwo html files by the Zhang-Shasha algorithm.\nThis package is based on [zss](https://github.com/timtadh/zhang-shasha).\n\n## Installation\n\nOS X & Linux:\n\nFrom PYPI\n\n```sh\n$ pip3 install vanguardkit\n```\n\nfrom the source\n\n```sh\n$ git clone https://github.com/dany2691/vanguard-kit.git\n$ cd vanguard-kit\n$ python3 setup.py install\n```\n\n## Usage example\n\nWith vanguard, it is possible to convert html content into a tree (graph) of nodes.\nThe create_html_tree function is the responsible to do that, it returns an instance of the VanguardNode class that inherits from the zss.Node class:\n\n```python\nfrom vanguardkit import create_html_tree\n\nwith open("target_website.html") as target_website:\n    thml_tree = create_html_tree(target_website)\n```\n\nIt is possible to segment specific parts of an html file.\n\nBy tag:\n```python\nwith open("target_website.html") as target_website:\n    html_tree = create_html_tree(\n        html_file=target_website,\n        specific_tag="footer"\n    )\n```\n\nBy tag and class:\n```python\nwith open("target_website.html") as target_website:\n    html_tree = create_html_tree(\n        html_file=target_website,\n        specific_tag="div",\n        class_="main-div"\n    )\n```\n\nBy tag and id:\n```python\nwith open("target_website.html") as target_website:\n    html_tree = create_html_tree(\n        html_file=target_website,\n        specific_tag="div",\n        id="super-div"\n    )\n```\n\n## Calculating distance\n\nAs previously said, the used algorithm is the Zhang-Shasha, that computes the edit distance between the two given trees. Ths is possible with the zss package behind the scenes; vanguard only provides a way to convert html files into trees.\n\n```python\nfrom vanguard_kit import create_html_tree, calcuate_html_tree_distance\n\nwith open("stored_target_website.html") as stored_file:\n    with open("current_target_website.html") as current_file:\n        previous_tree = create_html_tree(stored_file)\n        current_tree = create_html_tree(current_file)\n        print(calcuate_html_tree_distance(previous_tree, current_tree))\n        # Prints 1\n```\n\nDue to the VanguardNode class implements the __sub__ dunder method, the next way to calculate the edit distance is possible:\n\n```python\nfrom vanguard_kit import create_html_tree, calcuate_html_tree_distance\n\nwith open("stored_target_website.html") as stored_file:\n    with open("current_target_website.html") as current_file:\n        previous_tree = create_html_tree(stored_file)\n        current_tree = create_html_tree(current_file)\n        print(previous_tree - current_tree)\n        # Prints 1\n```\n\nThen, the next statement returns True:\n\n```python\ncalcuate_html_tree_distance(previous_tree, current_tree) == previous_tree - current_tree\n```\n\n# Development setup\n\nThis project uses __Poetry__ for dependecy resolution. It\'s a kind of mix between\npip and virtualenv. Follow the next instructions to setup the development enviroment.\n\nFirst of all, install Poetry:\n\n```sh\n$ pip install poetry\n```\n\n```sh\n$ git clone https://github.com/dany2691/vanguard-kit.git\n$ cd vanguard_kit\n$ poetry install\n```\n\nTo run the test-suite, inside the pybundler directory:\n\n```shell\n$ poetry run pytest test/ -vv\n```\n\n## Meta\n\nDaniel Omar Vergara Pérez – [@__danvergara __](https://twitter.com/__danvergara__) – daniel.omar.vergara@gmail.com -- [github.com/danvergara](https://github.com/danvergara)\n\nValery Briz - [@valerybriz](https://twitter.com/valerybriz) -- [github.com/valerybriz](https://github.com/valerybriz)\n\n## Contributing\n\n1. Fork it (<https://github.com/BentoBox-Project/vanguard-kit>)\n2. Create your feature branch (`git checkout -b feature/fooBar`)\n3. Commit your changes (`git commit -am \'Add some fooBar\'`)\n4. Push to the branch (`git push origin feature/fooBar`)\n5. Create a new Pull Request\n',
    'author': 'Daniel Omar Vergara Pérez',
    'author_email': 'daniel.omar.vergara@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
