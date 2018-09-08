/*
 * #!/usr/bin/env python
 * # -*- coding: UTF-8 -*-
 *
 * __license__ = """
 * Hackerfleet Operating System
 * ============================
 * Copyright (C) 2011- 2018 riot <riot@c-base.org> and others.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * """
 */

import angular from 'angular';
import uirouter from 'angular-ui-router';

import { routing } from './reporter.config.js';

import reportercomponent from './reporter/reporter.js';
import reportertemplate from './reporter/reporter.tpl.html';

import casebookcomponent from './casebook/casebook.js';
import casebooktemplate from './casebook/casebook.tpl.html';

export default angular
    .module('main.app.reporter', [uirouter])
    .config(routing)
    .component('reporter', {controller: reportercomponent, template: reportertemplate})
    .component('casebook', {controller: casebookcomponent, template: casebooktemplate})
    .name;
