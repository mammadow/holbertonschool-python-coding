#!/usr/bin/python3
"""
This module defines a square class
"""


class Square:
    """
    Represents a square with a private size attribute
    """

    def __init__(self, size):
        """
        Initializes a new square instance.

        Args:
            size: The size of the square (no type/value validation here).
        """
        self.__size = size
