#!/usr/bin/env python3
"""Module for 11-schools_by_topic.py"""


def schools_by_topic(mongo_collection, topic):
    """List of school having a specific topic
    
    Args:
        mongo_collection-collection to check
        topic[str] topic searched

    Returns:
        List
    """
    topics =  mongo_collection.find({"topic": topic})
    return topics
