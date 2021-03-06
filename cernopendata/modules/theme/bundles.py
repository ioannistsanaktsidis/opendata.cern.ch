# -*- coding: utf-8 -*-
#
# This file is part of CERN Open Data Portal.
# Copyright (C) 2017 CERN.
#
# CERN Open Data Portal is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# CERN Open Data Portal is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CERN Open Data Portal; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""JS/CSS bundles for theme."""

from __future__ import absolute_import, print_function

from flask_assets import Bundle
from invenio_assets import NpmBundle

css = NpmBundle(
    Bundle(
        'scss/styles.scss',
        filters='node-scss, cleancssurl',
    ),
    Bundle(
        'node_modules/angular-loading-bar/build/loading-bar.css',
        'node_modules/typeahead.js-bootstrap-css/typeaheadjs.css',
        # 'node_modules/bootstrap-switch/dist/css/bootstrap3'
        # '/bootstrap-switch.css',
        filters='cleancssurl',
    ),
    depends=('scss/*.scss', ),
    output='gen/cernopendata.%(version)s.css',
    npm={
        'angular-loading-bar': '~0.9.0',
        'bootstrap-sass': '~3.3.5',
        # 'bootstrap-switch': '~3.0.2',
        'font-awesome': '~4.4.0',
        'typeahead.js-bootstrap-css': '~1.2.1',
    }
)
"""Default CSS bundle."""

search_js = NpmBundle(
    'node_modules/angular-sanitize/angular-sanitize.js',
    'js/components/resultsBrief.js',
    output='gen/codp_search.%(version)s.js',
    npm={
        'angular': '~1.4.10',
        'angular-sanitize': '~1.4.14'
    },
)


visualise_js = NpmBundle(
    'node_modules/d3/d3.min.js',
    'node_modules/flot/jquery.flot.js',
    'node_modules/flot/jquery.flot.selection.js',
    'js/visualise/visualise_histograms.js',
    output='gen/cernopendata.%(version)s.js',
    npm={
        'd3': '^3.3.13',
        'flot': '~0.8.0-alpha',
    },
)

visualise_css = NpmBundle(
    'scss/visualise.scss',
    filters='node-scss, cleancss',
    output='gen/cernopendata.vis.%(version)s.css',
    npm={
        "bootstrap-sass": "~3.3.5",
    }
)
