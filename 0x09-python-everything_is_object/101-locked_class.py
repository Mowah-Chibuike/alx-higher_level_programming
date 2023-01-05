#!/usr/bin/python3
"""Module contains class LockedClass"""


class LockedClass:
    """LockedClass creates an object that prevents the user from dynamically
    creating object attributes, except if the instance is called first_name
    """
    def __setattr__(self, name, value):
        if name in self.__dict__ or name == 'first_name':
            self.__dict__[name] = value
    pass
