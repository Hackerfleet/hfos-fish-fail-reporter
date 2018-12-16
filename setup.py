#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# HFOS - Hackerfleet Operating System
# ===================================
# Copyright (C) 2011-2018 Heiko 'riot' Weinen <riot@c-base.org> and others.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

__author__ = "Heiko 'riot' Weinen"
__license__ = "AGPLv3"

from setuptools import setup, find_packages

setup(name="fishfail",
      version="0.0.1",
      description="FishFail - an Isomer module to coordinate and generate cases against IUU fishing",
      author="Hackerfleet Community",
      author_email="riot@c-base.org",
      url="https://github.com/hackerfleet/fishfail",
      license="GNU Affero General Public License v3",
      packages=find_packages(),
      long_description="""HFOS - FishFail
===============

A module to create, work on and publish case data to aid the battle against
illegal unregulated and unregistered fishing.

This software package is a plugin module for Isomer.
""",
      dependency_links=[],
      install_requires=[
          'isomer>=1.0.0',
          'hfos>=1.2.0'
      ],
      entry_points="""[isomer.components]
    reporter=hfos.reporter.reporter:Reporter
[isomer.schemata]
    report=hfos.reporter.report:Report
    case=hfos.reporter.case:Case
    blacklist=hfos.reporter.blacklist:Blacklist
    """,
      test_suite="tests.main.main",
      )
