#!/usr/bin/python3
"""
This module defines a square class
"""


class Square:
    """
    Represents a square with a private size attribute
    """
    @property
    def size(self):
        """
        Returns size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets value of size property
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

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
