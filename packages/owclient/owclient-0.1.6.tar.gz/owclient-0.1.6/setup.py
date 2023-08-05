# -*- coding: utf-8 -*-
# type: ignore
from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

packages = ['owclient', 'owclient.devices', 'owclient.exc']

package_data = {'owclient': ['py.typed'], '*': ['pyproject.toml']}

install_requires = ['pyownet>=0.10.0,<0.11.0']
setup(
    name='owclient',
    version='0.1.6',
    description=(
        'A light layer to use OWFS and pyownet with a more OOP approach.'),
    long_description=long_description,
    long_description_content_type='text/x-rst',
    author='Ferran Comabella',
    author_email='ferran@gmail.com',
    maintainer=None,
    maintainer_email=None,
    url='https://gitlab.com/fcomabella/ow-client',
    packages=packages,
    package_data=package_data,
    install_requires=install_requires,
    python_requires='>=3.8,<4.0',
    zip_safe=False,
)
