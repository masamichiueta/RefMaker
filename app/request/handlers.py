#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# RefMaker
# Copyright (C) 2012, Masamichi Ueta, Kyohei Ogawa
#

import os
import datetime
import base64
import hashlib
import hmac
from passlib.hash import sha512_crypt
from flask import Flask, request, redirect, url_for,render_template, abort
from werkzeug import secure_filename
from flask_security.utils import verify_password

from app import *
from tool.refmaker_dao import *
from tool.bibtex_io import *
from tool.exceptions import *


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'bib'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
           

account = RefmakerDao()
bibtex_file = BibTexIO() 

           
# Views
@app.route('/')
def root():
    if current_user.is_authenticated():
        user_id = current_user.get_id()
        user_directory = app.config['UPLOAD_FOLDER'] + '/' + str(user_id)
        if not os.path.isdir(user_directory):
            os.mkdir(user_directory)
        
        bibtex_directory = app.config['UPLOAD_FOLDER'] + '/' + str(user_id) + '/bibtex'
        if not os.path.isdir(bibtex_directory):
            os.mkdir(bibtex_directory) 
            
        icon_directory = app.config['UPLOAD_FOLDER'] + '/' + str(user_id) + '/icon'
        if not os.path.isdir(icon_directory):
            os.mkdir(icon_directory) 
            
        try:
            arg = request.args.get('page', '')
            if arg is not '':
                page = int(arg)
            else:
                page = 0
        except KeyError:
            page = 0
            
        pages = bibtex_file.count_pages()
        if page < 0 or pages < page:
            abort(404)
                
        user = account.get_user_by_id(user_id)
        bibtexlist = account.get_user_bibtexlist(user_id, page)
        
        
        return render_template('index.html', user = user,
                                             bibtexlist = bibtexlist,
                                             current_page = page,
                                             pages = int(pages))
    
    return render_template('index.html')
    
    
@app.route('/create_bibtex', methods=['GET','POST'])
def create_bibtex():
    if not current_user.is_authenticated():
        return redirect('/')
    
    if request.method == 'POST':
        bibtex_data = { 'created_by':None, 'bibtype_id':None, 'address':None, 'annote':None, 'author':None, 
                        'booktitle':None, 'chapter':None, 'crossref':None, 'edition':None, 'editor':None, 
                        'howpublished':None, 'institution':None, 'journal':None, 'key':None, 'month':None, 
                        'note':None, 'number':None, 'organization':None, 'pages':None, 'publisher':None, 
                        'school':None, 'series':None, 'title':None, 'type':None, 'volume':None, 
                        'year':None, 'yomi':None, 'file_path':None}

        user_id = current_user.get_id()
        bibtex_data['created_by'] = user_id
        bibtex_data['bibtype_id'] = int(request.form['bibtype_id'])
        
        date = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')
        
        bibtex_data['key'] = date
        
        if request.form.has_key('address'):
            bibtex_data['address'] = request.form['address']
        if request.form.has_key('annote'):
            bibtex_data['annote'] = request.form['annote']
        if request.form.has_key('author'):
            bibtex_data['author'] = request.form['author']
        if request.form.has_key('booktitle'):
            bibtex_data['booktitle'] = request.form['booktitle']
        if request.form.has_key('chapter'):
            bibtex_data['chapter'] = request.form['chapter']
        if request.form.has_key('corssref'):
            bibtex_data['crossref'] = request.form['crossref']
        if request.form.has_key('edition'):
            bibtex_data['edition'] = request.form['edition']
        if request.form.has_key('editor'):
            bibtex_data['editor'] = request.form['editor']
        if request.form.has_key('howpublished'):
            bibtex_data['howpublished'] = request.form['howpublished']
        if request.form.has_key('institution'):
            bibtex_data['institution'] = request.form['institution']
        if request.form.has_key('journal'):
            bibtex_data['journal'] = request.form['journal']
        if request.form.has_key('month'):
            bibtex_data['month'] = request.form['month']
        if request.form.has_key('note'):
            bibtex_data['note'] = request.form['note']
        if request.form.has_key('number'):
            bibtex_data['number'] = request.form['number']
        if request.form.has_key('organization'):
            bibtex_data['organization'] = request.form['organization']
        if request.form.has_key('pages'):
            bibtex_data['pages'] = request.form['pages']
        if request.form.has_key('publisher'):
            bibtex_data['publisher'] = request.form['publisher']
        if request.form.has_key('school'):
            bibtex_data['school'] = request.form['school']
        if request.form.has_key('series'):
            bibtex_data['series'] = request.form['series']
        if request.form.has_key('title'):
            bibtex_data['title'] = request.form['title']
        if request.form.has_key('type'):
            bibtex_data['type'] = request.form['type']
        if request.form.has_key('volume'):
            bibtex_data['volume'] = request.form['volume']
        if request.form.has_key('year'):
            bibtex_data['year'] = request.form['year']
        if request.form.has_key('yomi'):
            bibtex_data['yomi'] = request.form['yomi']
            
        
        
        #create bibtex file for export
        bibtex_directory = app.config['UPLOAD_FOLDER'] + '/' + str(user_id) + '/bibtex'
        if not os.path.isdir(bibtex_directory):
            os.mkdir(bibtex_directory) 
        
        
        file_name = date + '_bibtex.bib'
        file_path = str(user_id) + '/bibtex' + '/' + file_name
        
        bibtex_data['file_path'] = file_path
        
        
        bibtex_file.create_bibtex(bibtex_data)
    
        account.set_bibtex_data(bibtex_data)
        
    return redirect('/')
    
    
@app.route('/upload_bibtex', methods = ['GET', 'POST'])
def upload_bibtex():
    if not current_user.is_authenticated():
        return redirect('/')
        
    if request.method == 'POST':
    
        #upload bibtex file and add the information to database
        user_id = current_user.get_id()
        file = request.files['bibtex_file']
        
        if file and allowed_file(file.filename):
            bibtex_directory = app.config['UPLOAD_FOLDER'] + '/' + str(user_id) + '/bibtex'
            if not os.path.isdir(bibtex_directory):
                os.mkdir(bibtex_directory) 
                
            date = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')
           
            filename = date + '_bibtex' + os.path.splitext(file.filename)[1]        
           
            file.save(os.path.join(bibtex_directory, filename))
            file_path = bibtex_directory + '/' + filename
            
            bibtex_list = bibtex_file.parse_bibtex(file_path)
            if bibtex_list is None:
                return redirect('/bibtex_error')
            
            for bibtex_data in bibtex_list:
                bibtex_file.create_bibtex(bibtex_data)
                account.set_bibtex_data(bibtex_data)
            
            os.remove(file_path)
        else:
            bibtex_path = None
        
        
        return redirect('/')
    
    return redirect('/')
    

@app.route('/bibtex_error')
def bibtex_error():
    if not current_user.is_authenticated():
        return redirect('/')
        
    return render_template('bibtex_error.html')
    
    
@app.route('/export-all', methods = ['GET','POST'])
def export_all():
    if not current_user.is_authenticated():
        return redirect('/')
        
    user_id = current_user.get_id()
    
    if request.method == 'POST':
        follow_user_id = request.form['follow_user_id']
        bibtex_file.create_zip(follow_user_id)
        download_url = '/' + str(follow_user_id) + '/' + str(follow_user_id) + '_all.zip'
        return redirect(download_url)
        
    else:
        bibtex_file.create_zip(user_id)
        download_url = '/' + str(user_id) + '/' + str(user_id) + '_all.zip'
        return redirect(download_url)
    
    
@app.route('/delete', methods = ['GET','POST'])
def delete():
    if not current_user.is_authenticated():
        return redirect('/')
        
    if request.method == 'POST':
        bibtex_id = request.form['bibtex_id']
        bibtex = account.get_bibtex_by_id(bibtex_id)
        file_path = app.config['UPLOAD_FOLDER'] + '/' + bibtex.file_path
        os.remove(file_path)
        
        account.delete_bibtex(bibtex_id)
        return redirect('/')
    
    return redirect('/')
    

@app.route('/following')
def mylist():
    if not current_user.is_authenticated():
        return redirect('/')
    
    user_id = current_user.get_id()
    user = account.get_user_by_id(user_id)
    
    try:
        arg = request.args.get('page', '')
        if arg is not '':
            page = int(arg)
        else:
            page = 0
    except KeyError:
        page = 0
            
    pages = account.count_following_pages(user_id)
    if page < 0 or pages < page:
       abort(404)
    
    follow_list = account.get_paged_follow_by_id(user_id, page)
    
    return render_template('following.html', user = user,
                                             follow_list = follow_list,
                                             current_page = page,
                                             pages = int(pages))
                                             
                                             
@app.route('/user')
def user_page():
    if not current_user.is_authenticated():
        return redirect('/')
        
    try:
        arg = request.args.get('id', '')
        if arg is not '':
            follow_user_id = int(arg)
        else:
            follow_user_id = 0
    except KeyError:
        follow_user_id = 0
        
    try:
        arg = request.args.get('page', '')
        if arg is not '':
            page = int(arg)
        else:
            page = 0
    except KeyError:
        page = 0
    
    pages = bibtex_file.count_pages_by_user_id(follow_user_id)     
    if page < 0 or pages < page:
        abort(404)
        

    user_id = current_user.get_id()    
    user = account.get_user_by_id(user_id)
    current_user_follow_list = account.get_follow_by_id(user_id)
    follow_user = account.get_user_by_id(follow_user_id)
    follow_list = account.get_follow_by_id(follow_user_id)
    follower_list = account.get_follower_by_id(follow_user_id)
    bibtexlist = account.get_user_bibtexlist(follow_user_id, page)
        
    return render_template('follow_user.html', user = user,
                                               follow_user_id = follow_user_id,
                                               follow_user = follow_user,
                                               bibtexlist = bibtexlist,
                                               follow_list = follow_list,
                                               follower_list = follower_list,
                                               current_user_follow_list = current_user_follow_list,
                                               current_page = page,
                                               pages = int(pages))
                                               

@app.route('/follow', methods=['GET','POST'])
def follow():
    if not current_user.is_authenticated():
        return redirect('/')
        
    if request.method == 'POST':
        user_id = current_user.get_id()
        follow_id = request.form['follow_id']
        current_page = request.form['current_page']
        
        account.follow(user_id, follow_id)
        return redirect(current_page)


@app.route('/unfollow', methods=['GET','POST'])
def unfollow():
    if not current_user.is_authenticated():
        return redirect('/')
        
    if request.method == 'POST':
        user_id = current_user.get_id()
        follow_id = request.form['follow_id']
        current_page = request.form['current_page']
        
        account.unfollow(user_id, follow_id)
        
        return redirect(current_page)
                                
    
@app.route('/profile',methods=['GET','POST'])
def profile():
    if not current_user.is_authenticated():
        return redirect('/')
        
       
    user_id = current_user.get_id()
    user = account.get_user_by_id(user_id)
    follow_list = account.get_follow_by_id(user_id)
    follower_list = account.get_follower_by_id(user_id)
    
    try:
        duplicate_username = request.args['duplicate_username']
    except KeyError, e:
        duplicate_username = None
           
    return render_template('profile.html', user = user,
                                           follow_list = follow_list,
                                           follower_list = follower_list, duplicate_username=duplicate_username)


@app.route('/account_setting',methods=['GET','POST'])
def account_setting():
    if not current_user.is_authenticated():
        return redirect('/')
        
    if request.method == 'POST':
        user_id = current_user.get_id()
        user_name = request.form['user_name']
        if user_name is None:
            user_name = current_user.get_name()
        file = request.files['user_icon']
        icon_path = ''
        
        user = account.get_user_by_id(user_id)
        
        if user_name == '':
            user_name = user.name
        
        if file and allowed_file(file.filename):
            
            date = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')
           
            filename = date + '_icon' + os.path.splitext(file.filename)[1]
            icon_path = str(user_id) + '/icon/' + filename
            
            icon_dir = app.config['UPLOAD_FOLDER'] +'/' + str(user_id) + '/icon'
            
            if not os.path.isdir(icon_dir):
                os.mkdir(icon_dir)
                 
        else:
            icon_path = None
        
        try:
            account.update_user(user_id, name=user_name, icon_path=icon_path)
        except UserNameDuplicationError, e:
            print(e)
            return redirect('/profile?duplicate_username='+e.name)
        
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], icon_path))
                    
        return redirect('/profile')
            
    return redirect('/profile')
    
    
@app.route('/change_password', methods=['GET','POST'])
def change_password():
    if not current_user.is_authenticated():
        return redirect('/')
        
    if request.method == 'POST':
        user_id = current_user.get_id()
        user = account.get_user_by_id(user_id)
        
        if not verify_password(request.form['current_password'],user.password):
            return redirect('pass_error')
        
        new_h = hmac.new(app.config['SECURITY_PASSWORD_SALT'], request.form['new_password1'], hashlib.sha512)
        new_hash = base64.b64encode(new_h.digest())
        new_password = sha512_crypt.encrypt(new_hash)
                        
        account.update_user(user_id, password=new_password)
            
        return redirect('/profile')
            
    return redirect('/profile')
    
    
@app.route('/pass_error')
def pass_error():
    if not current_user.is_authenticated():
        return redirect('/')
        
    return render_template('pass_error.html')
    

@app.route('/userlist')
def user_list():
    if not current_user.is_authenticated():
        return redirect('/')
        
    if current_user.is_authenticated():
        user_id = current_user.get_id()
        user = account.get_user_by_id(user_id)
        
        try:
            arg = request.args.get('page', '')
            if arg is not '':
                page = int(arg)
            else:
                page = 0
        except KeyError:
            page = 0
            
        pages = account.count_all_users()
        if page < 0 or pages < page:
            abort(404)
        
        users = account.get_paged_all_users(page)
        
        follow_list = account.get_follow_by_id(user_id)
        
        return render_template('user_list.html', user = user,
                                                 users = users,
                                                 follow_list = follow_list,
                                                 current_page = page,
                                                 pages = int(pages))
                                                 

@app.route('/search', methods=['GET','POST'])
def search():
    if not current_user.is_authenticated():
        return redirect('/')
        
    if request.method == 'POST':
        search_text = request.form['search_text']
        user_id = current_user.get_id()
        user = account.get_user_by_id(user_id)
        follow_list = account.get_follow_by_id(user_id)
        users = account.get_searched_users(search_text)
        return render_template('user_list.html', user = user,
                                                 users = users,
                                                 follow_list = follow_list,
                                                 pages = 0)
        
        