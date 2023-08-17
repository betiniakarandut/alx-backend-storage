#!/usr/bin/env python3
"""Module for exercise.py"""
import redis
import uuid
from typing import Any, Union, Callable


class Cache:
    """store an instance of the Redis client as a private variable
    and flush the instance using flushdb.
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key: str = str(uuid.uuid1())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        """
        Retrieves a value from a Redis data storage
        """
        data = (self._redis).get(key)
        if fn is not None:
            return fn(data)
        else:
            return data

    def get_str(self, key: str) -> str:
        """
        Retrieves a string without a byte attached
        from a Redis data storage
        """
        return self.get(key).decode('utf-8')

    def get_int(self, key: Union[str, int]) -> int:
        """
        Retrieves an integer value from a Redis data storage
        """
        return int(self.get(key))
