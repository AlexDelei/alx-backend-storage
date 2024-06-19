#!/usr/bin/env python3
"""
Writing strings to redis
"""
import redis
import uuid


class Cache:
    """
    Set strings
    """
    def __init__(self):
        """
        Initialising by flushing the database first
        """
        self._redis = redis.Redis().flushdb()

    def store(self, data: int | str | float | bytes) -> str:
        """
        Generating a uuid and use it as a key in setting up the values
        """
        id = uuid.uuid4()
        r = redis.Redis()
        r.set(id, data)
        return id
