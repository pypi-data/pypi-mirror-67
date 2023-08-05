#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
from os import path
from setuptools import setup, find_packages
from m2r import parse_from_file

version_file = path.join(
    path.dirname(__file__),
    '__version__.py'
)

with open(version_file, 'r') as fp:
    m = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        fp.read(),
        re.M
    )
    version = m.groups(1)[0]


def _requirements():
    with open('requirements.txt', 'r') as fd:
        return [name.strip() for name in fd.readlines()]


readme_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'README.md')

print(parse_from_file(readme_file))


setup(
    name='lotify',
    version=version,
    description='Using Line Notify more easily',
    url='https://github.com/louis70109/line-notify',
    author='NiJia Lin',
    author_email='louis70109@gmail.com',
    maintainer="NiJia Lin",
    maintainer_email="louis70109@gmail.com",
    long_description=parse_from_file(readme_file),
    long_description_content_type="text/x-rst",
    keywords='line notify python lotify',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=_requirements(),
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    project_urls={
        'Bug Reports': 'https://github.com/louis70109/lotify/issues',
        'Source': 'https://github.com/louis70109/lotify',
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        'License :: OSI Approved :: MIT License',
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development"
    ],
)
