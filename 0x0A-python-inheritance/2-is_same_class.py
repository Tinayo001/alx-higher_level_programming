#!/usr/bin/python3
"""determines whether an object is an instance of a class"""


def is_same_class(obj, a_class):
    """checks if an object is an instance of a class

    Args:
    obj: the object to be checked against a class
    a_class: the class to check whether the object is instance of the class.

    Returns:
    returns True if the object is exactly an instance of the specified class;
    returns false.
    """

    if type(obj) == (a_class):
        return True
    else:
        return False
