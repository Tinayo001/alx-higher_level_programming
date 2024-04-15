#!/usr/bin/python3
"""defines an object attribute lookup function"""


def lookup(obj):
    """return a list of an object attribute"""
    return dir(obj)
