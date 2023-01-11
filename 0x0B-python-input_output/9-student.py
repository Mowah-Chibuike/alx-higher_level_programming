#!/usr/bin/python3
"""
Module contains the Student class
"""


class Student:
    """
    class Student defines a student by:
        - Public instance sttributes:
            - first_name
            - last_name
            - age
        - Instantiation with first_name, last_name and age
        - Public method def to_json(self): that retrieves a dictionary repre\
sentation of a Student instance
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves the dictionary representation of the object
        """
        return dict(self.__dict__)
