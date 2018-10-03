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
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * """
 */

'use strict';

import deletionWarning from '../modals/deletionWarning.tpl.html';

class casebookComponent {

    constructor(objectproxy, user, $state, $scope, socket, modal) {
        this.op = objectproxy;
        this.user = user;
        this.state = $state;
        this.scope = $scope;
        this.socket = socket;
        this.modal = modal;

        this.cases = {};
        this.reports = [];
        this.reports_by_id = {};
        this.vessels = {};
        this.users = {};

        this.checked_reports = [];
        this.deletion_candidates = [];

        this.all_reports = false;

        let self = this;

        this.getData = function () {
            self.op.search('case', '', '*').then(function(msg){
                let cases = msg.data.list;
                console.log('[CASE] Cases:', cases);
                for (let item of cases) {
                    self.cases[item.uuid] = item;
                }
            });
            self.op.search('report', '', '*').then(function(msg){
                let reports = msg.data.list;
                console.log('[CASE] Reports:', reports);
                for (let item of reports) {
                    self.reports.push(item);
                    self.reports_by_id[item.uuid] = item;
                }
            });
            self.op.search('vessel', '', '*').then(function(msg){
                let vessels = msg.data.list;
                for (let item of vessels) {
                    self.vessels[item.uuid] = item;
                }
            });
            self.op.search('user', '', 'name').then(function(msg){
                let users = msg.data.list;
                for (let item of users) {
                    self.users[item.uuid] = item;
                }
            })

        };

        if (this.user.signedin === true) {
            console.log('User signed in. Getting data.');
            this.getData();
        } else {
            console.log('Not logged in apparently, heres this:', this.user);
        }

        this.create_case = function(uuid) {
            console.log('Creating case from report:', uuid);
            let vessel = self.reports_by_id[uuid].vessel;
            let initial_object = {
                vessel: vessel,
                reporter: self.reports_by_id[uuid].owner,
                report: uuid
            };
            self.state.go('app.editor', {schema: 'case', initial: initial_object, action: 'Create'})
        }


        $scope.$on('User.Login', this.getData);
    }


    delete(uuid) {
        this.deletion_candidates = [uuid];

        this.modal({
            template: deletionWarning,
            scope: this.scope,
            title: 'Really delete reports?',
            keyboard: false,
            id: 'deletionWarningDialog'
        });
    }


    confirm_deletion() {
        for (let uuid of this.deletion_candidates) {
            console.log('Deleting report:', uuid);
            this.op.deleteObject('report', uuid);
        }

        this.deletion_candidates = [];
        this.checked_reports = {};
        this.all_reports = false;
    }

    act_reports() {
        this.deletion_candidates = [];

        for (let uuid of Object.keys(this.checked_reports)) {
            if (this.checked_reports[uuid] === true) {
                this.deletion_candidates.push(uuid);
            }
        }

        this.modal({
            template: deletionWarning,
            scope: this.scope,
            title: 'Really delete users?',
            keyboard: false,
            id: 'deletionWarningDialog'
        });
    }
}

casebookComponent.$inject = ['objectproxy', 'user', '$state', '$scope', 'socket', '$modal'];

export default casebookComponent;
