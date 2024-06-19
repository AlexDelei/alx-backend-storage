#!/usr/bin/env python3
"""
Writing strings to redis
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Set strings
    """
    def __init__(self):
        """
        Initialising by flushing the database first
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[int, str, float, bytes]) -> str:
        """
        Generating a uuid and use it as a key in setting up the values
        """
        id = uuid.uuid4()
        self._redis.set(str(id), data)
        return str(id)
