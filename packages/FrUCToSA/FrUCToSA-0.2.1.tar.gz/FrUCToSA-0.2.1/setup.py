#!/bin/env python

#######################################################################
# Copyright (C) 2020 David Palao
#
# This file is part of FrUCToSA.
#
#  FrUCToSA is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  FrUCToSA is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with FrUCToSA.  If not, see <http://www.gnu.org/licenses/>.
#
#######################################################################

import os

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

def get_requirements():
    """Find the required packages from a 'single source of truth' (tm)."""
    req_file_name = os.path.join(here, "requirements", 'production.text')
    with open(req_file_name, encoding='utf-8') as f:
        reqs = [_.strip() for _ in f]
    return reqs


setup(
    name="FrUCToSA",
    version="0.2.1",
    #use_scm_version={"write_to": os.path.join("fructosa", "version.py")},
    #use_scm_version={"version_scheme": "post-release"},
    #version="0.2.1",
    #setup_requires=['setuptools_scm'],
    description="A package to collect and analyze basic performance data from clusters",
    long_description=long_description,
    author="David Palao",
    author_email="palao@csc.uni-frankfurt.de",
    url="https://itp.uni-frankfurt.de/~palao/software/FrUCToSA",
    license='GNU General Public License (GPLv3)',
    packages=find_packages(),
    provides=["fructosa"],
    install_requires=get_requirements(),
    platforms=['GNU/Linux'],
    entry_points={'console_scripts': [
        "fructosad = fructosa.fructosad:main",
        "lagent = fructosa.lagent:main",
        "lmaster = fructosa.lmaster:main",
        "make-fructosa-dashboard = fructosa.grafana.dashboard:make_dashboard",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: No Input/Output (Daemon)",
        "Framework :: AsyncIO",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: System :: Monitoring",
    ],
    #test_suite="tests",
)
