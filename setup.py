# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from divio_wagtail_home import __version__


setup(
    name='divio-wagtail-home',
    version=__version__,
    description=open('README.rst').read(),
    author='Wagtail Community',
    author_email='None',
    packages=find_packages(),
    platforms=['OS Independent'],
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
)
