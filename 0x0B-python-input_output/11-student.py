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
        - Public method def to_json(self, attrs=None): that retrieves a dicti\
onary representation of a Student instance
        - Public method def reload_from_json(self, json): that replaces all a\
ttributes of the Student instance
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves the dictionary representation of the object
        """
        new_repr = {}
        is_list_of_str = True
        if isinstance(attrs, list):
            for string in attrs:
                if not isinstance(string, str):
                    is_list_of_str = False
        else:
            is_list_of_str = False

        if is_list_of_str:
            for name, value in self.__dict__.items():
                if name in attrs:
                    new_repr.__setitem__(name, value)
            return new_repr
        else:
            return dict(self.__dict__)

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        """
        for name, value in json.items():
            self.__dict__.__setitem__(name, value)
