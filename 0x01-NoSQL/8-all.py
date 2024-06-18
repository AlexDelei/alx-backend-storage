#!/usr/bin/env python3
"""
Listing all documents using pymongo
"""


def list_all(mongo_collection):
    """
    
    mongo_collection -- MongoDB documents collection
    """
    
    return mongo_collection.find()
