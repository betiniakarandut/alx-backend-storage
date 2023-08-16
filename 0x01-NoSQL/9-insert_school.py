#!/usr/bin/env python3
"""Module for 9-insert_school.py"""


def insert_school(mongo_collection, **kwargs):
    """Inserts new document

    Args:
        mongo_collection: collection to check

    Returns:
       new _id
    """
    new_docs = mongo_collection.insert_one(kwargs)
    return new_docs.inserted_id
