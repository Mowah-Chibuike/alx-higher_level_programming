#!/usr/bin/python3
import json
"""
Module contains the add_item function
"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item():
    """
    adds all arguments to a Python list, and then save them to a file
    """
    from sys import argv
    args = argv[1:]
    is_empty = False
    with open("add_item.json", "a+", encoding='utf-8') as json_file:
        json_file.seek(0, 0)
        if json_file.read() == "":
            is_empty = True

    if is_empty:
        new = []
    else:
        new = load_from_json_file("add_item.json") + args
    save_to_json_file(new, "add_item.json")


if __name__ == "__main__":
    add_item()
