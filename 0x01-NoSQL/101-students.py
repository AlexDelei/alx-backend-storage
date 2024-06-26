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
            '$unwind': '$topics'
        },
        {
            '$group': {
                '_id': '$_id',
                'name': {'$first': '$name'},
                'averageScore': {'$avg': '$topics.score'}
            }
        },
        {
            '$sort': {'averageScore': -1}
        }
    ]
    result = mongo_collection.aggregate(pipeline)
    return list(result)
