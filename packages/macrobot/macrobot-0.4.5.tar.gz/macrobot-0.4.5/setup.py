# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['macrobot', 'macrobot.tests']

package_data = \
{'': ['*']}

install_requires = \
['jinja2>=2.10.3,<3.0.0',
 'numpy>=1.18.3,<2.0.0',
 'opencv-python>=4.2.0,<5.0.0',
 'pytest>=5.4.1,<6.0.0',
 'scikit-image>=0.16.2,<0.17.0']

entry_points = \
{'console_scripts': ['mb = macrobot.cli:main']}

setup_kwargs = {
    'name': 'macrobot',
    'version': '0.4.5',
    'description': 'Macrobot is an image analysis software for studying plant-pathogen interactions on macroscopic level.',
    'long_description': None,
    'author': 'Stefanie Lueck',
    'author_email': 'lueck@ipk-gatersleben.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
