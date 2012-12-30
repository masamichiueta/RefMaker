#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# RefMaker
# Copyright (C) 2012, Masamichi Ueta, Kyohei Ogawa
#

import os
import sys
import ConfigParser

# Set main configuration file's path.
refmaker_conf_file = os.path.join(os.path.dirname(__file__), '../config/refmaker.ini')

# Set virtualenv configuration file's path.
virtualenv_conf_file = os.path.join(os.path.dirname(__file__), '../config/virtualenv.ini')

sys.stdout = sys.stderr

os.environ['REFMAKER_CONFIG'] = refmaker_conf_file

if os.path.isfile(virtualenv_conf_file):
    conf = ConfigParser.SafeConfigParser()
    conf.read(virtualenv_conf_file)
    activate_this = conf.get('virtualenv', 'VIRTUALENV_ACTIVATE')
    execfile(activate_this, dict(__file__=activate_this))

from app import app as application
