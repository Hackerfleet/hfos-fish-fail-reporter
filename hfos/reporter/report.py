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

Schema: Report
==============

Contains
--------

Report - against IUU fishery

"""

from hfos.schemata.defaultform import editbuttons, lookup_field, create_object
from hfos.schemata.base import base_object, uuid_object

reportSchema = base_object('report', all_roles='crew')

reportSchema['properties'].update({
    'vessel': uuid_object(title='Vessel', description='Select a Vessel'),
    'notes': {'type': 'string', 'format': 'html',
              'title': 'User notes',
              'description': 'Additional notes and remarks'},
    'noticed': {
        'type': 'string', 'format': 'datetimepicker', 'title': 'Date & Time',
        'description': 'When did you notice the vessel'
    },
    'reason': {
        'type': 'string', 'title': 'Reason', 'description': 'Reason for report'
    }
})

reportForm = [
    {
        'type': 'section',
        'htmlClass': 'row',
        'items': [
            {
                'type': 'section',
                'htmlClass': 'col-xs-6',
                'items': [
                    'noticed', 'reason'
                ]
            },
            {
                'type': 'section',
                'htmlClass': 'col-xs-6',
                'items': [
                    lookup_field('vessel'), create_object('vessel', 'vessel')
                ]
            },
        ]
    },
    'notes',
    editbuttons
]

Report = {'schema': reportSchema, 'form': reportForm}
