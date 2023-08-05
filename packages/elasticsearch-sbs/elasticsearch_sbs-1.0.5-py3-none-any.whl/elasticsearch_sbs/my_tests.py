# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 05:22:59 2020

@author: User
"""
from elasticsearch import Elasticsearch
from elasticsearch_sbs import part_one as p_1

host = 'https://search-covid198-es-2-x6zr2th7oiq7sjzp653cs3k3xm.eu-west-1.es.amazonaws.com/'
region = 'eu-west-1'
es = Elasticsearch(
    hosts=host,
)

p_1.es_version()








