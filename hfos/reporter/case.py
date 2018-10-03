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

"""

Schema: Case
============

Contains
--------

Case - against IUU fishery

"""

from hfos.schemata.defaultform import editbuttons, lookup_field
from hfos.schemata.base import base_object, uuid_object

caseSchema = base_object('case', all_roles='crew')

caseSchema['properties'].update({
    'report': uuid_object(title='Report', description='Associated report'),
    'reporter': uuid_object(title='Reporter', description='Reporting user'),
    'vessel': uuid_object(title='Vessel', description='Select a Vessel'),
    'evidence': {
        'type': 'array',
        'items': {
            'type': 'object',
            'properties': {
                'evidence_type': {
                    'type': 'string',
                    'enum': ['photo', 'video', 'ais-track', 'satellite-image', 'witness-report', 'inspection']
                },
                #'details': {
                #    'type': uuid_object(title='Details', description='Evidence details')
                #}
            }
        }
    },
    'notes': {'type': 'string', 'format': 'html', 'title': 'User notes',
              'description': 'Entry notes'}
})

caseForm = [
    'name',
    {
        'type': 'section',
        'htmlClass': 'row',
        'items': [

            {
                'type': 'section',
                'htmlClass': 'col-xs-6',
                'items': [
                    lookup_field('report')
                ]
            },
            {
                'type': 'section',
                'htmlClass': 'col-xs-6',
                'items': [
                    lookup_field('reporter', 'user')
                ]
            },
            {
                'type': 'section',
                'htmlClass': 'col-xs-6',
                'items': [
                    lookup_field('vessel'),
                ]
            },
        ]
    },
    'evidence',
    editbuttons
]

Case = {'schema': caseSchema, 'form': caseForm}
