#!/usr/bin/env python3
"""
Find a school with a certain topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    find by topic

    mongo_collection -- pymongo collection object
    topic -- search by this topic
    """

    results = mongo_collection.find({'topics': topic})
    return results
