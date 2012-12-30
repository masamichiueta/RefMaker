#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# RefMaker
# Copyright (C) 2012, Masamichi Ueta, Kyohei Ogawa
#

import os
import re
import datetime
import codecs
import math
import zipfile
from pybtex.database.input import bibtex
from flask.ext.security import current_user
from flask import redirect

from app import app


class BibTexIO:

    def parse_bibtex(self, import_file_path):
        parser=bibtex.Parser()
        bib_datas=parser.parse_file(import_file_path)
        user_id = current_user.get_id()
    
        bibtex_list = []
        file_index = 0 
    
        for key in bib_datas.entries.keys():
            tmp_bib_data = bib_datas.entries[key]
            bibtex_data = { 'created_by':None, 'bibtype_id':None, 'address':None, 'annote':None, 'author':None, 
                            'booktitle':None, 'chapter':None, 'crossref':None, 'edition':None, 'editor':None, 
                            'howpublished':None, 'institution':None, 'journal':None, 'key':None, 'month':None, 
                            'note':None, 'number':None, 'organization':None, 'pages':None, 'publisher':None, 
                            'school':None, 'series':None, 'title':None, 'type':None, 'volume':None, 
                            'year':None, 'yomi':None, 'file_path':None}
                            
            bibtex_data['created_by'] = user_id
            bibtex_data['key'] = key
            
            date = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')
            file_name = date + '_' + str(file_index) + '_bibtex.bib'
            file_path = str(user_id) + '/bibtex' + '/' + file_name
            
            bibtex_data['file_path'] = file_path
            
            if tmp_bib_data.type == 'article':
                bibtex_data['bibtype_id'] = 1
            elif tmp_bib_data.type == 'book':
                bibtex_data['bibtype_id'] = 2
            elif tmp_bib_data.type == 'booklet':
                bibtex_data['bibtype_id'] = 3
            elif tmp_bib_data.type == 'inbook':
                bibtex_data['bibtype_id'] = 4
            elif tmp_bib_data.type == 'incollection':
                bibtex_data['bibtype_id'] = 5
            elif tmp_bib_data.type == 'inproceedings':
                bibtex_data['bibtype_id'] = 6
            elif tmp_bib_data.type == 'conference':
                bibtex_data['bibtype_id'] = 7
            elif tmp_bib_data.type == 'manual':
                bibtex_data['bibtype_id'] = 8
            elif tmp_bib_data.type == 'masterthesis':
                bibtex_data['bibtype_id'] = 9
            elif tmp_bib_data.type == 'phdthesis':
                bibtex_data['bibtype_id'] = 10
            elif tmp_bib_data.type == 'proceedings':
                bibtex_data['bibtype_id'] = 11
            elif tmp_bib_data.type == 'techreport':
                bibtex_data['bibtype_id'] = 12
            elif tmp_bib_data.type == 'unpublished':
                bibtex_data['bibtype_id'] = 13
            elif tmp_bib_data.type == 'misc':
                bibtex_data['bibtype_id'] = 14
            else:
                return None
	        
            bibtex_data.update(tmp_bib_data.fields)
	        
            if bibtex_data['month'] == 'jan':
                bibtex_data['month'] = 'January'
            elif bibtex_data['month'] == 'feb':
                bibtex_data['month'] = 'February'
            elif bibtex_data['month'] == 'mar':
                bibtex_data['month'] = 'March'
            elif bibtex_data['month'] == 'apr':
                bibtex_data['month'] = 'April'
            elif bibtex_data['month'] == 'may':
                bibtex_data['month'] = 'May'
            elif bibtex_data['month'] == 'jun':
                bibtex_data['month'] = 'June'
            elif bibtex_data['month'] == 'jul':
                bibtex_data['month'] = 'July'
            elif bibtex_data['month'] == 'aug':
                bibtex_data['month'] = 'August'
            elif bibtex_data['month'] == 'sep':
                bibtex_data['month'] = 'September'
            elif bibtex_data['month'] == 'oct':
                bibtex_data['month'] = 'October'
            elif bibtex_data['month'] == 'nov':
                bibtex_data['month'] = 'November'
            elif bibtex_data['month'] == 'dec':
                bibtex_data['month'] = 'December'
	            
            if tmp_bib_data.persons.has_key('author'):
                authors = tmp_bib_data.persons['author']
                author_list = []
	        
                for author in authors:
                    author_name = unicode(author)
                    author_list.append(author_name)
        
                author_str = author_list[0]
                del author_list[0]
                if len(author_list) > 0:
                    for author in author_list:
                        if author == author_list[-1]:
                            author_str = author_str + ', and ' + author
                        else:
                            author_str = author_str + ', ' + author
                
                bibtex_data['author'] = author_str
                
            bibtex_list.append(bibtex_data)
            
            file_index += 1
	        
        return bibtex_list
    

    def create_bibtex(self, data):
    
        file_path = app.config['UPLOAD_FOLDER'] + '/' + data['file_path']
        file = codecs.open(file_path,'w','utf-8')
        
        if data['bibtype_id'] == 1:
            file.write('@article{ ')
            
        if data['bibtype_id'] == 2:
            file.write('@book{ ')
        
        if data['bibtype_id'] == 3:
            file.write('@booklet{ ')
            
        if data['bibtype_id'] == 4:
            file.write('@inbook{ ')
            
        if data['bibtype_id'] == 5:
            file.write('@incollection{ ')
            
        if data['bibtype_id'] == 6:
            file.write('@inproceedings{ ')
            
        if data['bibtype_id'] == 7:
            file.write('@conference{ ')
            
        if data['bibtype_id'] == 8:
            file.write('@manual{ ')
            
        if data['bibtype_id'] == 9:
            file.write('@masterthesis{ ')
            
        if data['bibtype_id'] == 10:
            file.write('@phdthesis{ ')
            
        if data['bibtype_id'] == 11:
            file.write('@proceedings{ ')
            
        if data['bibtype_id'] == 12:
            file.write('@techreport{ ')
            
        if data['bibtype_id'] == 13:
            file.write('@unpublished{ ')
            
        if data['bibtype_id'] == 14:
            file.write('@misc{ ')
        
        file.write(data['key'])

        if data['address'] is not None and data['address'] != '':
            address = ',\n' + 'address = "' + data['address'] + '"'
            file.write(address)
            
        if data['annote'] is not None and data['annote'] != '':
            annote = ',\n' + 'annote = "' + data['annote'] + '"'
            file.write(annote)
            
        if data['author'] is not None and data['author'] != '':
            author_list = self.format_author(data['author'])
            author = ',\n' + 'author = "' + author_list + '"'
            file.write(author)
        
        if data['booktitle'] is not None and data['booktitle'] != '':
            booktitle = ',\n' + 'booktitle = "' + data['booktitle'] + '"'
            file.write(booktitle)
        
        if data['chapter'] is not None and data['chapter'] != '':
            chapter = ',\n' + 'chapter = "' + str(data['chapter']) + '"'
            file.write(chapter)
            
        if data['crossref'] is not None and data['crossref'] != '':
            crossref = ',\n' + 'crossref = "' + data['crossref'] + '"'
            file.write(crossref)
            
        if data['edition'] is not None and data['edition'] != '':
            edition = ',\n' + 'edition = "' + data['edition'] + '"'
            file.write(edition)
            
        if data['editor'] is not None and data['editor'] != '':
            editor = ',\n' + 'editor = "' + data['editor'] + '"'
            file.write(editor)
            
        if data['howpublished'] is not None and data['howpublished'] != '':
            howpublished = ',\n' + 'howpublished = "' + data['howpublished'] + '"'
            file.write(howpublished)
            
        if data['institution'] is not None and data['institution'] != '':
            institution = ',\n' + 'institution = "' + data['institution'] + '"'
            file.write(institution)
            
        if data['journal'] is not None and data['journal'] != '':
            journal = ',\n' + 'journal = "' + data['journal'] + '"'
            file.write(journal)
            
        if data['month'] is not None and data['month'] != '':
            _month = self.format_month(data['month'])
            month = ',\n' + 'month = "' + _month + '"'
            file.write(month)
            
        if data['note'] is not None and data['note'] != '':
            note = ',\n' + 'note = "' + data['note'] + '"'
            file.write(note)
        
        if data['number'] is not None and data['number'] != '':
            number = ',\n' + 'number = "' + str(data['number']) + '"'
            file.write(number)
            
        if data['organization'] is not None and data['organization'] != '':
            organization = ',\n' + 'organization = "' + data['organization'] + '"'
            file.write(organization)
            
        if data['pages'] is not None and data['pages'] != '':
            pages = ',\n' + 'pages = "' + data['pages'] + '"'
            file.write(pages)
            
        if data['publisher'] is not None and data['publisher'] != '':
            publisher = ',\n' + 'publisher = "' + data['publisher'] + '"'
            file.write(publisher)
            
        if data['school'] is not None and data['school'] != '':
            school = ',\n' + 'school = "' + data['school'] + '"'
            file.write(school)
                    
        if data['series'] is not None and data['series'] != '':
            series = ',\n' + 'series = "' + data['series'] + '"'
            file.write(series)
            
        if data['title'] is not None and data['title'] != '':
            title = ',\n' + 'title = "' + data['title'] + '"'
            file.write(title)
            
        if data['type'] is not None and data['type'] != '':
            type = ',\n' + 'type = "' + data['type'] + '"'
            file.write(type)
            
        if data['volume'] is not None and data['volume'] != '':
            volume = ',\n' + 'volume = "' + str(data['volume']) + '"'
            file.write(volume)
            
        if data['year'] is not None and data['year'] != '':
            year = ',\n' + 'year = "' + str(data['year']) + '"'
            file.write(year)

        if data['yomi'] is not None and data['yomi'] != '':
            yomi = ',\n' + 'yomi = "' + data['yomi'] + '"'
            file.write(yomi)
        
        file.write('\n}')
        file.close()
        
        
    def create_zip(self, user_id):
        
        file_dir = app.config['UPLOAD_FOLDER'] + '/' + user_id + '/bibtex/'
        zip_dir = app.config['UPLOAD_FOLDER'] + '/' + user_id + '/'
        zip_path = zip_dir + user_id + '_all.zip'
        
        if os.path.isfile(zip_path):
            os.remove(zip_path)
        
        zip = zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED)
        
        files = os.listdir(file_dir)
        
        for file in files:
            each_file_path = file_dir + file
            zip.write(each_file_path, file)
            
        zip.close()
        
        
    def format_author(self, authors):
        tmp_authors_list = re.split(', |and',authors)
        while tmp_authors_list.count('') > 0:
            tmp_authors_list.remove('')
        
        author_list = ''
        
        for tmp_author in tmp_authors_list:
            author = tmp_author.strip()
            if len(author_list) != 0:
                author_list += ' and ' + author
            else:
                author_list += author

        return author_list
        
       
    def format_month(self, month):
    
        _month = ''
        if month == 'January':
            _month = 'jan'
            
        if month == 'February':
            _month = 'feb'
        
        if month == 'March':
            _month = 'mar'
        
        if month == 'April':
            _month = 'apr'
        
        if month == 'May':
            _month = 'may'
        
        if month == 'June':
            _month = 'jun'
            
        if month == 'July':
            _month = 'jul'
            
        if month == 'August':
            _month = 'aug'
            
        if month == 'September':
            _month = 'sep'
            
        if month == 'October':
            _month = 'oct'
            
        if month == 'November':
            _month = 'nov'
            
        if month == 'December':
            _month = 'dec'
            
        return _month
        
    def count_pages(self):
        user_id = current_user.get_id()
        bibtex_dir = app.config['UPLOAD_FOLDER'] + '/' + str(user_id) + '/bibtex'
        num_by_page = app.config['NUM_BY_PAGE']

        pages = 0
        for f in os.listdir(bibtex_dir)[::-1]:
            if not os.path.isfile(bibtex_dir + '/' + f):
                continue
            pages += 1

        return math.ceil(float(pages) / num_by_page)
        
    def count_pages_by_user_id(self, user_id):
        bibtex_dir = app.config['UPLOAD_FOLDER'] + '/' + str(user_id) + '/bibtex'
        num_by_page = app.config['NUM_BY_PAGE']

        pages = 0
        for f in os.listdir(bibtex_dir)[::-1]:
            if not os.path.isfile(bibtex_dir + '/' + f):
                continue
            pages += 1

        return math.ceil(float(pages) / num_by_page)