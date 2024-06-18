#!/usr/bin/env python3
"""
Inserting a document in pymongo
"""


def insert_school(mongo_collection, **kwargs):
    """
    Creating a collection with pymongo

    mongo_collection -- pymongo collection object
    kwargs -- key, value items. Its a dict
    """
    data = mongo_collection.insert_one(kwargs)

    return data.inserted_id
