# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 21:12:14 2017

@author: alana
"""
import json
from pprint import pprint
import sys

def read_json(file_path):
    """
    converts json file to dictionary.
    
    param file_path: path to the json file to parse
    returns: a json object of the json (may contain sub-dictionaries as well)
    throws: file_not_found exceptions
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
        
    return data

if __name__ == '__main__':
    pprint(read_json(sys.argv[1]))
