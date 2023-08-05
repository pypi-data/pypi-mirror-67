#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 04:11:06 2020

@author: Sara Ben Shabbat
"""

import elasticsearch

def print_es_version() -> None:    
    print(elasticsearch.VERSION)
        
    