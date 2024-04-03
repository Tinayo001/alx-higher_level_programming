#!/usr/bin/python3
"""defines a class Square
    Raises:
        TypeError:size must be an integer
        ValueError:size must be >= 0
    Returns:
    Area:area of square for both original and initial size
    """


class Square:
    """represents a class square"""
    def __init__(self, size=0):
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        """determines and returns the area"""
        return(self.__size * self.__size)
