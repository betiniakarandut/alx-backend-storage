#!/usr/bin/env python3
"""Module for 101-students.py"""


def top_students(mongo_collection):
    """All students sorted by average score

    Args:
        mongo_collection-database collection

    Returns:
        all students sorted by average score
    """
    pipeline = mongo_collection.aggregate([
        {
            "$group": {
                "_id": None,
                "averageScore": {"$avg": "$score"}
            }
        },
        {
            "$sort": {'averageScore': -1}
        }
    ])
    return pipeline
