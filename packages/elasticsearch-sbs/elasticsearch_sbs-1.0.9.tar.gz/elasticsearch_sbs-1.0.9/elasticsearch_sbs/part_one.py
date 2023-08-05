#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 04:11:07 2020

@author: Sara Ben Shabbat
"""
import elasticsearch
from elasticsearch import Elasticsearch

def get_es_version() -> tuple:    
    return elasticsearch.VERSION

def is_es_active(es: Elasticsearch) -> bool:
    if es.ping():
        return True
    else:
        return False
    
def get_es_indexes(es: Elasticsearch) -> list:
    return list(es.indices.get_alias().keys())

def get_index_ids(es: Elasticsearch, index: str) -> list:
    res = es.search(
    index=index,    
    body={"query": {"match_all": {}}, "size": 10000, "_source": False })

    ids = [document['_id'] for document in res['hits']['hits']]
    return ids

