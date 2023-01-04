#!/usr/bin/python3
"""
Module contains the text_indentation function
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    
    Prototype: def text_indentation(text)

    text must be a string, otherwise raise a TypeError exception with the
    message text must be a string
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    flag = False
    for i in range(len(text)):
        if text[i] != " ":
            flag = True
        if text[i] in ":?.":
            print(f"{text[i]}\n")
            flag = False
        elif flag:
            print(text[i], end="") 
