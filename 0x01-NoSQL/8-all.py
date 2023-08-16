#!/usr/bin/env python3
"""Module for 8-all.py"""


def list_all(mongo_collection):
    """Lists all documents in a collection."""
    if not mongo_collection:
        return[]
    list_doc = []
    for db in mongo_collection.find():
        list_doc.append(db)
    return list_doc
