#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 04:11:07 2020

@author: Sara Ben Shabbat
"""
import elasticsearch
from elasticsearch import Elasticsearch

def es_version() -> tuple:    
    return elasticsearch.VERSION

def is_es_active(es: Elasticsearch) -> bool:
    if es.ping():
        return True
    else:
        return False
    
def es_indexes(es: Elasticsearch) -> list:
    return list(es.indices.get_alias().keys())

