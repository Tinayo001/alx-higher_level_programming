#!/usr/bin/python3
"A module that prints a class named Mylist"""


class MyList(list):
    """defines a MyList class that inherits from list
    Attr:
    attr1: prints a sorted list in assending order
    """

    def print_sorted(self):
        """Represent an instance"""
        print(sorted(self))
