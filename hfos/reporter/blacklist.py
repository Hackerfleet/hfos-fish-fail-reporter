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

Schema: Blacklist
============

Contains
--------

Blacklist - against IUU fishery

"""

from hfos.schemata.defaultform import editbuttons, lookup_field
from hfos.schemata.base import base_object, uuid_object

blacklistSchema = base_object('blacklist', all_roles='crew')

blacklistSchema['properties'].update({
    'imo': {
        'type': 'string',
        'title': 'IMO Id', 'description': 'Blacklisted IMO identity'
    },
    'vessel': uuid_object(title='Vessel', description='Blacklisted vessel details'),
    'report': uuid_object(title='Report', description='Associated report'),
    'blacklist': uuid_object(title='Blacklist', description='Associated blacklist file'),
    'notes': {'type': 'string', 'format': 'html', 'title': 'User notes',
              'description': 'Entry notes'}
})

blacklistForm = [
    {
        'type': 'section',
        'htmlClass': 'row',
        'items': [
            {
                'type': 'section',
                'htmlClass': 'col-xs-6',
                'items': [
                    'name', 'imo', 'vessel'
                ]
            },
            {
                'type': 'section',
                'htmlClass': 'col-xs-6',
                'items': [
                    lookup_field('report'), lookup_field('blacklist')
                ]
            },
        ]
    },
    'notes'
]

Blacklist = {'schema': blacklistSchema, 'form': blacklistForm}
