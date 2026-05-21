#!/usr/bin/env python3

"""Python function that returns all students sorted by average score"""


def top_students(mongo_collection):
    ''' return avg score'''
    return mongo_collection.aggregate(
        [
            {"$addFields": {"averageScore": {"$avg": "$topics.score"}}},
            {"$sort": {"averageScore": -1}},
        ]
    )
