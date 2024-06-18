#!/usr/bin/env python3
"""
Sorting all students by their average scores

hint: db.collection.aggregate()
"""


def top_students(mongo_collection):
    """
    Sorting all students by their sort
    """

    pipeline = [
        {
            'averageScore': {'$avg': '$score'}
        },
        {
            '$sort': {'averageScore': -1}
        }
    ]
    mongo_collection.aggregate(pipeline)
    return
