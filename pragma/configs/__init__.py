#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__init__.py
~~~~~~~~~~~

:copyright: (c) 2015 by Anonymous.
:license: see LICENSE for more details.
"""

import os
import sys
import types
try:
    import ConfigParser as configparser
except:
    import configparser

path = os.path.dirname(os.path.realpath(__file__))
approot = os.path.abspath(os.path.join(path, os.pardir))

def getdef(self, section, option, default_value):
    try:
        return self.get(section, option)
    except:
        return default_value

config = configparser.ConfigParser()
config.read('%s/settings.cfg' % path)
config.getdef = types.MethodType(getdef, config)

HOST = config.getdef("server", "host", '0.0.0.0')
PORT = int(config.getdef("server", "port", 8080))
DEBUG = bool(int(config.getdef("server", "debug", 1)))
template_folder = 'static/app/views'
options = {
    'debug': DEBUG,
    'host': HOST,
    'port': PORT,
}

# Enable CORS to allow cross-domain loading of tilesets from this server
# Especially useful for SeaDragon viewers running locally
cors = bool(int(config.getdef('server', 'cors', 0)))

# DATABASES
DB_URI = '%(dbn)s://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % {
    'dbn': config.getdef('db', 'dbn', 'postgres'),
    'port': config.getdef('db', 'port', '5432'),
    'host': config.getdef('db', 'host', 'localhost'),
    'user': config.getdef('db', 'user', 'pragmabot'),
    'db': config.getdef('db', 'db', 'pragma'),
    'pw': config.getdef('db', 'pw', '')
}

WAYBACK_SERVER = "http://web.archive.org"
