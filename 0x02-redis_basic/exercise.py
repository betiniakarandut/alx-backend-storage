#!/usr/bin/env python3
"""Module for exercise.py"""
import redis
import uuid
from typing import Any


class Cache:
    """store an instance of the Redis client as a private variable
    and flush the instance using flushdb.
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float]) -> str:
        key: str = str(uuid.uuid1())
        self._redis.set(key, data)
        return key
