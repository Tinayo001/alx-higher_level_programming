#!/usr/bin/python3
"""Represents a class rectangle that initializes private
instances of width and height


    Raises:
    TypeError: both values must return and integer values
    ValueError: both values must be greater than 0

    Returns: The original values and and new values of width and height
"""


class Rectangle:
    """Represents a class rectangle"""

    def __init__(self, width=0, height=0):

        """initializes a class rectangle

        Args:
        width(int): new value of width.Default value set to 0
        height(): new value of height.Default value set to 0
        """
        
        self.width = width
        self.height = height

    @property
    def height(self):
        """represents the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the new value of the height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """represents the widht of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the new value of a rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
