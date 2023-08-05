#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["Click", "sqlalchemy"]

setup_requirements = ["pytest-runner", ]

test_requirements = ["pytest", ]

# with open("requirements.txt") as f:
#     requirements = f.read().splitlines()

# with open("requirements_test.txt") as f:
#     test_requirements = f.read().splitlines()

setup(  # pragma: no cover
    author="Roberto Preste",
    author_email="robertopreste@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="La riffa e la raffa python package.",
    entry_points={
        "console_scripts": [
            "riffaraffa=riffaraffa.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords="riffaraffa",
    name="riffaraffa",
    packages=find_packages(include=["riffaraffa"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/robertopreste/riffaraffa",
    version='0.2.0',
    zip_safe=False,
)
