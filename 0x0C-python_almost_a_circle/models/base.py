#!/usr/bin/python3
"""
Module contains the Base Class
"""
import json


class Base:
    """
    Base class holds an id for all instances
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Runs when a new instance is created
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries:
            - list_dictionaries is a list of dictionaries
            - If list_dictionaries is None or empty, return the string: "[]"
            - Otherwise, returns the JSON string representation of list_\
dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file:
            - list_objs is a list of instances who inherits of Base - examp\
le: list of Rectangle or list of Square instances
            - If list_objs is None, saves an empty list
            - The filename is: <Class name>.json - example: Rectangle.json
            - overwrites the file if it already exists
        """
        list_objects = []
        if list_objs is not None:
            for obj in list_objs:
                list_objects.append(obj.to_dictionary())

        with open(
            '{}.json'.format(cls.__name__), 'w+', encoding='utf-8') as a_file:
            string = cls.to_json_string(list_objects)
            a_file.write(string)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation
        """
        if json_string is None:
            return ""
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        list_instances = []
        with open(
            '{}.json'.format(cls.__name__), "a+", encoding='utf-8') as a_file:
            a_file.seek(0, 0)
            list_dict = cls.from_json_string(a_file.readline())

        if type(list_dict) is list:
            for item in list_dict:
                list_instances.append(cls.create(**item))

        return list_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        serializes objects to csv files
        """
        list_tuples = []
        if cls.__name__ == "Rectangle":
            keys = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            keys = ["id", "size", "x", "y"]
        if list_objs is not None:
            for item in list_objs:
                obj_tuple = ()
                obj_dict = item.to_dictionary()
                for key in keys:
                    obj_tuple += (obj_dict[key],)
                list_tuples.append(obj_tuple)

        with open(
            '{}.csv'.format(cls.__name__), "w+", encoding='utf-8') as a_file:
            for item in list_tuples:
                delim = ''
                for i in item:
                    a_file.write('{}{}'.format(delim, i))
                    delim = ','
                a_file.write('\n')

    @classmethod
    def load_from_file_csv(cls):
        """
        deserializes objects from csv files
        """
        list_obj = []
        with open(
            '{}.csv'.format(cls.__name__), 'a+', encoding='utf-8') as a_file:
            a_file.seek(0, 0)
            lines = a_file.readlines()
        print(lines)
        for line in lines:
            dummy = cls(1, 1)
            attr_list = [int(x) for x in line.split(',')]
            attr_tuple = tuple(attr_list)
            dummy.update(*attr_tuple)
            list_obj.append(dummy)

        return list_obj
