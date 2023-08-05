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
    'version': '0.1.1',
    'description': 'Dynamic mode decompositon in python.',
    'long_description': '.. image:: https://readthedocs.org/projects/dmdlab/badge/?version=latest\n   :target: https://dmdlab.readthedocs.io/en/latest/?badge=latest\n   :alt: Documentation Status\n  \n.. image:: https://img.shields.io/badge/License-MIT-blue.svg\n   :target: https://lbesson.mit-license.org/\n   :alt: MIT License\n \nDynamic mode decomposition (DMD)is a tool for analyzing the dynamics of nonlinear systems.\n\nThis is an experimental DMD codebase for research purposes.\n\nAlternatively, check out `PyDMD <https://mathlab.github.io/PyDMD/>`_, a professionally maintained open source DMD\ncodebase for Python.\n\nInstallation:\n\n.. code-block:: python\n\n    pip install dmdlab\n\nUsage:\n\n.. code-block:: python\n\n    from dmdlab import DMD, plot_eigs\n    import numpy as np\n    from scipy.linalg import logm\n\n    # Generate toy data\n    ts = np.linspace(0,6,50)\n\n    theta = 1/10\n    A_dst = np.array([[np.cos(theta), -np.sin(theta)],\n                      [np.sin(theta), np.cos(theta)]])\n    A_cts = logm(A_dst)/(ts[1]-ts[0])\n\n    x0 = np.array([1,0])\n    X = np.vstack([expm(A_cts*ti)@x0 for ti in ts]).T\n\n    # Fit model\n    model = DMD.from_full(X, ts)\n\n    # Print the eigenvalue phases\n    print(np.angle(model.eigs))\n\n    >>> [0.1, -0.1]\n\n\nFor a technical reference, check out the `DMD book <http://www.dmdbook.com/>`_.\n',
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
