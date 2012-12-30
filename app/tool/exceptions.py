#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# RefMaker
# Copyright (C) 2012, Masamichi Ueta, Kyohei Ogawa
#

class UserNameDuplicationError(Exception):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name + ' is already used!'