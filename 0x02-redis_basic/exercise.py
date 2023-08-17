#!/usr/bin/env python3
"""Module for exercise.py"""
import redis
import uuid
from functools import wraps
from typing import Any, Union, Callable


def count_calls(method: Callable) -> Callable:
    """
    Decorator function that takes in a callable
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """increment count"""
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator function to store the history of inputs
      and outputs for a function
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Store inputs and outputs in Redis lists"""
        if isinstance(self._redis, redis.Redis):
            inputs_key = f"{method.__qualname__}:inputs"
            outputs_key = f"{method.__qualname__}:outputs"

            # Store input arguments
            self._redis.rpush(inputs_key, str(args))

            # Call the original method and get the output
            result = method(self, *args, **kwargs)

            # Store the output
            self._redis.rpush(outputs_key, str(result))

            return result
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """store an instance of the Redis client as a private variable
    and flush the instance using flushdb.
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
