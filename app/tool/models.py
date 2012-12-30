#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# RefMaker
# Copyright (C) 2012, Masamichi Ueta, Kyohei Ogawa
#

from flask.ext.security import Security, SQLAlchemyUserDatastore, \
     UserMixin, RoleMixin
from flask.ext.sqlalchemy import SQLAlchemy

from app import app

db = SQLAlchemy(app)
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

def setup_flask_security():
    # Setup Flask-Security
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)
    
    #db.create_all()
    return


# Define models
class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), default='username')
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    icon_path = db.Column(db.String(255), default='img/default.png')
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def __str__(self):
        return '<User id=%s email=%s>' % (self.id, self.email)

class Bibtex(db.Model):
    __tablename__ = 'bibtex'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_by = db.Column(db.Integer)
    bibtype_id = db.Column(db.Integer, db.ForeignKey('bibtype.id'), nullable=False)
    address = db.Column(db.String(255))
    annote = db.Column(db.String(255))
    author = db.Column(db.String(255))
    booktitle = db.Column(db.String(255))
    chapter = db.Column(db.String(45))
    crossref = db.Column(db.String(45))
    edition = db.Column(db.String(45))
    editor = db.Column(db.String(255))
    howpublished = db.Column(db.String(45))
    institution = db.Column(db.String(45))
    journal = db.Column(db.String(45))
    key = db.Column(db.String(45))
    month = db.Column(db.String(10))
    note = db.Column(db.String(255))
    number = db.Column(db.String(45))
    organization = db.Column(db.String(45))
    pages = db.Column(db.String(45))
    publisher = db.Column(db.String(45))
    school = db.Column(db.String(45))
    series = db.Column(db.String(45))
    title = db.Column(db.String(255))
    type = db.Column(db.String(45))
    volume = db.Column(db.String(45))
    year = db.Column(db.String(45))
    yomi = db.Column(db.String(45))
    file_path = db.Column(db.String(45))
    
class Bibtype(db.Model):
    __tablename__ = 'bibtype'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), nullable=False, unique=True)
    
class Follow(db.Model):
    __tablename__ = 'follow'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    who = db.Column(db.Integer)
    whom = db.Column(db.Integer)
    
    __table_args__ = (db.UniqueConstraint('who', 'whom'),)
    
    def __init__(self, who, whom):
        self.who = who
        self.whom = whom

class MustItem(db.Model):
    __tablename__ = 'must_item'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type_id = db.Column(db.Integer, nullable=False)
    item_name = db.Column(db.String(45), nullable=False)
    
    __table_args__ = (db.UniqueConstraint('type_id', 'item_name'),)

    
        
    

        

    

