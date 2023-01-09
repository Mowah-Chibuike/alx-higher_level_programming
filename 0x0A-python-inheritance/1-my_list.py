#!/usr/bin/python3
"""
Module holds a class MyList which is a subclass of list
"""


class MyList(list):
    """
    class MyList is a subclass of the list class... It also has a \
print_sorted method
    """
    def print_sorted(self):
        """
        method to print itself in ascending order
        """
        print(sorted(self))
