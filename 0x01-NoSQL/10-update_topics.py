#!/usr/bin/env python3
"""
Updating content with pymongo
"""


def update_topics(mongo_collection, name, topics):
    """
    Update my db

    mongo_collection -- pymongo collection object
    name -- school name to update
    topics -- list of topics approached in the school
    """

    query_name = {name: name}
    new_values = {'$set': 
            {'topics': topics}
        }
    mongo_collection.update_many(query_name, new_values)
    return

