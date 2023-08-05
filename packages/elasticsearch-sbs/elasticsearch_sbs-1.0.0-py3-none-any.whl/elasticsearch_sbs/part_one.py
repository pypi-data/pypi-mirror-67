#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 04:11:07 2020

@author: Sara Ben Shabbat
"""

import elasticsearch

def get_elasticsearch_version() -> tuple:    
    return elasticsearch.VERSION

