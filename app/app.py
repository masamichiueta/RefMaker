#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# RefMaker
# Copyright (C) 2012, Masamichi Ueta, Kyohei Ogawa
#

import os
import sys
from flask import Flask, Response
from flask import render_template, request, session, abort, redirect, url_for
from flask.ext.babel import Babel
from flask.ext.mail import Mail
from flask.ext.security import LoginForm, current_user, login_required, \
     login_user
from werkzeug import SharedDataMiddleware



app = Flask(__name__)

try:
    app.config.from_envvar('REFMAKER_CONFIG')
except RuntimeError:
    app.debug   = True
    app.testing = True
    app.config['SECRET_KEY'] = 'super-secret'
    app.config['SECRET_KEY'] = 'super-secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite'
    app.config['DEFAULT_MAIL_SENDER'] = 'info@site.com'
    app.config['SECURITY_REGISTERABLE'] = True
    app.config['SECURITY_CONFIRMABLE'] = True
    app.config['SECURITY_RECOVERABLE'] = True
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT']  = 465
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = 'test'
    app.config['MAIL_PASSWORD'] = 'test'
    app.config['SECURITY_PASSWORD_HASH'] = 'plaintext'
    app.config['SECURITY_PASSWORD_SALT'] = 'sample test here'
    app.config['SECURITY_POST_LOGIN_VIEW'] = '/'
    app.config['UPLOAD_FOLDER'] = 'path/to/uploads'
    app.config['NUM_BY_PAGE'] = 10
    
        
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
        '/': os.path.join(os.path.dirname(__file__), 'static')
        })
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
        '/': os.path.join(os.path.dirname(__file__), 'uploads')
        })

# Setup mail extension
mail = Mail(app)


#init refmaker db
from tool.models import *
setup_flask_security()

#Request Handlers
from request.handlers import *


if __name__ == '__main__':
    app.run()
