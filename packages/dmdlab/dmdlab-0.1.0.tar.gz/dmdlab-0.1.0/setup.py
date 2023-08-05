# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dmdlab']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.2.1,<4.0.0', 'numpy>=1.18.3,<2.0.0', 'scipy>=1.4.1,<2.0.0']

extras_require = \
{'docs': ['sphinx>=3.0.2,<4.0.0', 'nbsphinx>=0.6.1,<0.7.0'],
 'test': ['pytest>=5.2,<6.0']}

setup_kwargs = {
    'name': 'dmdlab',
    'version': '0.1.0',
    'description': 'Dynamic mode decompositon in python.',
    'long_description': '.. image:: https://readthedocs.org/projects/pydmd/badge/?version=latest\n  :target: https://pydmd.readthedocs.io/en/latest/?badge=latest\n  :alt: Documentation Status\n  \n.. image:: https://img.shields.io/badge/License-MIT-blue.svg\n   :target: https://lbesson.mit-license.org/\n   :alt: MIT License\n \nDynamic mode decomposition (DMD)is a tool for analyzing the dynamics of nonlinear systems.\n \n.. rubric:: References\n.. [TRLB14] Tu, J.H.; Rowley, C.W.; Luchtenburg, D.M.; Brunton, S.L.; Kutz, J.N.: On dynamic mode decomposition,  Theory and applications. In: Journal of Computational Dynamics\n\n',
    'author': 'Andy Goldschmidt',
    'author_email': 'andygold@uw.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
