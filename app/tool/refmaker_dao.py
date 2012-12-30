#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# RefMaker
# Copyright (C) 2012, Masamichi Ueta, Kyohei Ogawa
#

import datetime
import math

from models import *
from exceptions import *

from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from app import app


class RefmakerDao:

    #def __init__(self):

    def get_user_by_id(self, user_id):

        return self._get_user_by_id(user_id)
        

    def _get_user_by_id(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        
        return user
        

    def get_user_by_name(self, name):
        return self._get_user_by_name(name)


    def _get_user_by_name(self, name):
        user = User.query.filter_by(name=name).first()       
        
        return user            
            
    def update_user(self, user_id,
               name=None, email=None, password=None, icon_path=None):
        if name == 'username':
            raise  UserNameDuplicationError('username')
        
        user = self._get_user_by_id(user_id)
        
        query = User.query.filter_by(name=name)
        try:
            another_user = query.one()
            if another_user.id != user.id:
                raise  UserNameDuplicationError(name)
                return
        except MultipleResultsFound, e:
            raise UserNameDuplicationError('username')
            return
        except NoResultFound, e:
            pass
                
        if user == None:
            return

        if not name == None:
            user.name = name
        if not email == None:
            user.email = email
        if not password == None:
            user.password = password
        if not icon_path == None:
            user.icon_path = icon_path
        
        db.session.commit()
    
    
    def set_bibtex_data(self, data):
        

        bibtex_obj = Bibtex()
        
        bibtex_obj.created_by = data['created_by']
        bibtex_obj.bibtype_id = data['bibtype_id']
        bibtex_obj.address = data['address']
        bibtex_obj.annote = data['annote']
        bibtex_obj.author = data['author']
        bibtex_obj.booktitle = data['booktitle']
        bibtex_obj.chapter = data['chapter']
        bibtex_obj.crossref = data['crossref']
        bibtex_obj.edition = data['edition']
        bibtex_obj.editor = data['editor']
        bibtex_obj.howpublished = data['howpublished']
        bibtex_obj.institution = data['institution']
        bibtex_obj.journal = data['journal']
        bibtex_obj.key = data['key']
        bibtex_obj.month = data['month']
        bibtex_obj.note = data['note']
        bibtex_obj.number = data['number']
        bibtex_obj.organization = data['organization']
        bibtex_obj.pages = data['pages']
        bibtex_obj.publisher = data['publisher']
        bibtex_obj.school = data['school']
        bibtex_obj.series = data['series']
        bibtex_obj.title = data['title']
        bibtex_obj.type = data['type']
        bibtex_obj.volume = data['volume']
        bibtex_obj.year = data['year']
        bibtex_obj.yomi = data['yomi']
        bibtex_obj.file_path = data['file_path']

        db.session.add(bibtex_obj)

        db.session.commit()
       

    def get_bibtex_by_id(self, bibtex_id):

        return self._get_bibtex_by_id(bibtex_id)
        

    def _get_bibtex_by_id(self, bibtex_id):
        bibtex = Bibtex.query.filter_by(id=bibtex_id).first()
        
        return bibtex
        
    def get_user_bibtexlist(self, user_id, page):

        return self._get_user_bibtexlist(user_id, page)
        

    def _get_user_bibtexlist(self, user_id, page):
        offset = app.config['NUM_BY_PAGE'] * page
        bibtexlist = Bibtex.query.filter_by(created_by=user_id).order_by(Bibtex.id.desc()).offset(offset).limit( app.config['NUM_BY_PAGE'] ).all()
        
        return bibtexlist
        
    def delete_bibtex(self, bibtex_id):

        bibtex = self._get_bibtex_by_id(bibtex_id)
        
        if bibtex == None:
            return

        db.session.delete(bibtex)
        db.session.commit()
        
    def get_follow_by_id(self, user_id):
        follows = Follow.query.filter_by(who=user_id).order_by(Follow.id.desc()).all()
        
        follow_list = []
        for follow in follows:
            user = self._get_user_by_id(follow.whom)
            follow_list.append(user)
        
        return follow_list
        
    def get_paged_follow_by_id(self, user_id, page):
        offset = app.config['NUM_BY_PAGE'] * page
        follows = Follow.query.filter_by(who=user_id).order_by(Follow.id.desc()).offset(offset).limit( app.config['NUM_BY_PAGE'] ).all()
        follow_list = []
        for follow in follows:
            user = self._get_user_by_id(follow.whom)
            follow_list.append(user)
        
        return follow_list
        
    def count_following_pages(self, user_id):
        follow_list = self.get_follow_by_id(user_id)
        num_by_page = app.config['NUM_BY_PAGE']
        pages = len(follow_list)
        return math.ceil(float(pages) / num_by_page)
        
        
    def get_follower_by_id(self, user_id):
        followers = Follow.query.filter_by(whom=user_id).order_by(Follow.id.desc()).all()
        
        follower_list = []
        
        for follower in followers:
            user = self._get_user_by_id(follower.who)
            follower_list.append(user)
        
        return follower_list
        
        
    def follow(self, user_id, follow_id):
        follow_obj = Follow(user_id, follow_id)
      
        db.session.add(follow_obj)
        db.session.commit()
    
    
    def unfollow(self,user_id, follow_id):
        unfollow = Follow.query.filter_by(who=user_id).filter_by(whom=follow_id).first()
        
        if unfollow == None:
            return 
            
        db.session.delete(unfollow)
        db.session.commit()
    
    
    def get_all_users(self):
        users = User.query.order_by(User.id.desc()).all()
        return users
        
    def get_paged_all_users(self, page):
        offset = app.config['NUM_BY_PAGE'] * page
        users = User.query.order_by(User.id.desc()).offset(offset).limit(app.config['NUM_BY_PAGE']).all()
                
        return users
        
    def count_all_users(self):
        users = self.get_all_users()
        num_by_page = app.config['NUM_BY_PAGE']
        pages = len(users)
        return math.ceil(float(pages) / num_by_page)
        
    def get_searched_users(self, search_text):
        users = User.query.filter_by(name=search_text).all()
        return users
        
    
        
        