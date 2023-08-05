# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lipo']

package_data = \
{'': ['*']}

install_requires = \
['dlib>=19.19.0,<20.0.0', 'scikit-learn>=0.22.1']

setup_kwargs = {
    'name': 'lipo',
    'version': '1.0.0',
    'description': 'Global, derivative-free optimization',
    'long_description': 'LIPO is a package for derivative-free, global optimization. Is based on\nthe `dlib` package and provides wrappers around its optimization routine.',
    'author': 'Jan Beitner',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jdb78/lipo',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
