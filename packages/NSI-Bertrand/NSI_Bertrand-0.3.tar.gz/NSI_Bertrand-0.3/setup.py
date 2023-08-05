#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    name='NSI_Bertrand',
    version='0.3',
    description='Fonctions et outils pour la NSI',
    author='Benjamin Bertrand',
    author_email='benjamin.bertrand@ac-lyon.fr',
    packages=['NSI_Bertrand'],
    )
