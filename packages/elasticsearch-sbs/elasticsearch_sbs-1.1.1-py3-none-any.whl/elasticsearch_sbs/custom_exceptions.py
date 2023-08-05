# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 06:38:30 2020

@author: Sara Ben Shabbat
"""

class NoExistIndexError(Exception):
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        super().__init__(message)


