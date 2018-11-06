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


Module: Reporter
================

Component to manage case related actions and publish blacklist data


"""

from isomer.component import ConfigurableComponent, handler
from isomer.database import objectmodels
from isomer.logger import isolog, error, warn, critical, events
from isomer.events.system import authorized_event
from pprint import pprint


class Reporter(ConfigurableComponent):
    """
    Manages case related actions
    """
    channel = 'isomer-web'

    configprops = {
    }

    def __init__(self, *args):
        """
        Initialize the Reporter component.

        :param args:
        """

        super(Reporter, self).__init__("REPORTER", *args)

        self.log("Started")

        self.blacklist = {}

    #@handler()
    #def authorized_event_handler(self, event, *args, **kwargs):
    #    self.log(event, args, kwargs)
        #if isinstance(event, authorizedevent):
        #    self.log('Event:', event)
        #    account = self.accounts[event.useruuid]
        #    self.log('Account', account)