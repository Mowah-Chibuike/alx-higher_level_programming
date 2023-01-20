#!/usr/bin/python3
"""
Module contains the Base Class
"""
import json
import turtle


class Base:
    """
    The Base Class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        run whenever an instance is created
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns JSON repreentation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the json representation of list_objs to a file
        """
        list_objects = []
        if list_objs is not None:
            for obj in list_objs:
                list_objects.append(obj.to_dictionary())

        with open(
                '{}.json'.format(
                cls.__name__), 'w+', encoding='utf-8') as a_file:
            string = cls.to_json_string(list_objects)
            a_file.write(string)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances
        """
        list_objs = []
        with open(
                '{}.json'.format(
                cls.__name__), 'a+', encoding='utf-8') as a_file:
            a_file.seek(0, 0)
            list_dict = cls.from_json_string(a_file.read())

        for item in list_dict:
            new = cls.create(**item)
            list_objs.append(new)

        return list_objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        serializes a subclass of Base to a CSV file
        """
        list_tuples = []
        if cls.__name__ == "Rectangle":
            keys = ["id", "width", "height", "x", "y"]
        elif cls.__name__ == "Square":
            keys = ["id", "size", "x", "y"]
        if list_objs is not None:
            for obj in list_objs:
                obj_tuple = ()
                obj_dict = obj.to_dictionary()
                for key in keys:
                    obj_tuple += (obj_dict[key],)
                list_tuples.append(obj_tuple)

        with open(
                '{}.csv'.format(
                cls.__name__), "w+", encoding='utf-8') as a_file:
            for item in list_tuples:
                delim = ''
                for i in item:
                    a_file.write('{}{}'.format(delim, i))
                    delim = ','
                a_file.write('\n')

    @classmethod
    def load_from_file_csv(cls):
        """
        deserializes a list of subclasses of the Base clas
        """
        list_obj = []
        with open(
                '{}.csv'.format(
                cls.__name__), 'a+', encoding='utf-8') as a_file:
            a_file.seek(0, 0)
            list_csv = a_file.readlines()

        for item in list_csv:
            obj_tuple = ()
            attr_list = item.split(',')
            for i in attr_list:
                obj_tuple += (int(i),)
            dummy = cls(1, 1)
            dummy.update(*obj_tuple)
            list_obj.append(dummy)

        return list_obj

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        draws all rectangles and squares in the respective list_rectangles \
list_squares lists which contains instances of the Rectangle and Square \
classes respectively
        """
        pen = turtle.Turtle()
        for rectangle in list_rectangles:
            rect_dict = rectangle.to_dictionary()
            pen.penup()
            pen.color('blue')
            pen.setposition(rect_dict["x"], rect_dict["y"])
            pen.pendown()
            pen.setheading(0)
            for i in range(2):
                pen.forward(rect_dict["width"])
                pen.right(90)
                pen.forward(rect_dict["height"])
                pen.right(90)

        for square in list_squares:
            square_dict = square.to_dictionary()
            pen.penup()
            pen.color("green")
            pen.setposition(square_dict["x"], square_dict["y"])
            pen.pendown()
            pen.setheading(0)
            for i in range(4):
                pen.forward(square_dict["size"])
                pen.right(90)
        turtle.done()
