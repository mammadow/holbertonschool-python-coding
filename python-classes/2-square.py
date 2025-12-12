#!/usr/bin/python3
"""
This module defines a square class
"""


class Square:
    """
    Represents a square with a private size attribute
    """

    def area(self):
        """
        Returns area of square
        """
        return self.__size**2

    def __init__(self, size=0):
        """
        Initializes a new square instance.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is < 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
