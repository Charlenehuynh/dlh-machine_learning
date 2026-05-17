#!/usr/bin/env python3

"""Python function that lists all documents in a collection"""


def list_all(mongo_collection):
    """List all documnts in given MongoDB collection"""

    if mongo_collection is None:
        return []
    result = []
    collection = mongo_collection.find()
    for i in collection:
        result.append(i)
    return result
