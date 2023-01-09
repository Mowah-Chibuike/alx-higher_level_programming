#!/usr/bin/python3
"""
Module contains the class MyInt
"""


class MyInt(int):
    """
    Class MyInt a subclass of the int class. It is a rebel. MyInt has == and \
!= operators inverted
    """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
