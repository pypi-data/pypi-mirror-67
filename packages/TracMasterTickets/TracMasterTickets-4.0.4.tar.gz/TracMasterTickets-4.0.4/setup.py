#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2007-2012 Noah Kantrowitz <noah@coderanger.net>
# Copyright (c) 2013-2016 Ryan J Ollos <ryan.j.ollos@gmail.com>
#
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#

import os
from setuptools import find_packages, setup

setup(
    name='TracMasterTickets',
    version='4.0.4',
    packages=find_packages(exclude=['*.tests']),
    package_data={
        'mastertickets': [
            'htdocs/img/*.gif',
            'htdocs/img/*.png',
            'htdocs/js/*.js',
            'htdocs/css/*.css',
            'templates/*.html'
        ]
    },

    author='Noah Kantrowitz',
    author_email='noah@coderanger.net',
    maintainer='Ryan J Ollos',
    maintainer_email='ryan.j.ollos@gmail.com',
    description='Provides ticket dependencies and master tickets.',
    license='BSD 3-Clause',
    keywords='trac plugin ticket dependencies master',
    url='https://trac-hacks.org/wiki/MasterTicketsPlugin',
    classifiers=[
        'Framework :: Trac',
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],

    install_requires=['Trac'],
    test_suite='mastertickets.tests.suite',
    entry_points={
        'trac.plugins': [
            'mastertickets.api = mastertickets.api',
            'mastertickets.web_ui = mastertickets.web_ui',
        ]
    }
)
