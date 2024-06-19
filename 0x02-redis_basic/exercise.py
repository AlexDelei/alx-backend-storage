#!/usr/bin/env python3
"""
Writing strings to redis
"""
import redis
import uuid
from typing import Union, Callable, Optional, Any


class Cache:
    """
    Cache class to interact with Redis python API
    """
    def __init__(self) -> None:
        """
        Initialising by flushing the database first
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[int, str, float, bytes]) -> str:
        """
        Store the input data in Redis with a randomly generated UUID key

        Args:
            data (Union[int, str, float, bytes]): Data to be stored in Redis

        Returns:
            str: The UUID key under which the data is stored
        """
        id = str(uuid.uuid4())
        self._redis.set(id, data)
        return id

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """
        Retreives the data using the key

        Args:
            key (str): the object key to be used to retreive data.
            fn (Callable): function that converts bytes data types to normal

        Returns:
            value: the value with their correct data types
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Coonverts bytes to string data type
        """
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: int) -> Optional[int]:
        """
        Converting bytes to integer data type
        """
        return self.get(key, fn=int)
