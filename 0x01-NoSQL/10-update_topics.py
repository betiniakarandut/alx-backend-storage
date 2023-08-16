#!/usr/bin/env python3
"""Module 10-update_topics.py"""


def update_topics(mongo_collection, name, topics):
    """Update topics base on name

    Args:
        mongo_collection - collection to check
        name[string] to match
        topics[list] to update

    Returns:
        updated topics
    """
    match = {"name": name}
    update_match = {"$set": {"topics": topics}}
    update = mongo_collection.update_many(match, update_match)
    return update
