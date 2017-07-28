# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

setup(
    name='pytemplate',
    version='0.0.1',
    description='Skeleton for python module',
    long_description=readme,
    author='Quadyster',
    author_email='',
    url='https://github.com/gsakhila/Skeleton-python-project',
    packages=find_packages(exclude=('tests', 'docs'))
)
