# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['seodo']

package_data = \
{'': ['*']}

install_requires = \
['certifi==2020.4.5.1',
 'chardet==3.0.4',
 'click==7.1.1',
 'future==0.18.2',
 'requests==2.23.0',
 'tabulate==0.8.7',
 'typer[all]>=0.1.1,<0.2.0']

entry_points = \
{'console_scripts': ['seodo = seodo.main:app']}

setup_kwargs = {
    'name': 'seodo',
    'version': '0.0.13',
    'description': 'Seo.do terminal client',
    'long_description': 'An SEO cli that helps SEO professionals to organize keywords by different grouping algorithms. Coming soon: data collection from various sources.\n\n',
    'author': 'Seo Do',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
