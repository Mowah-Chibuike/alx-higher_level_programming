#!/usr/bin/python3
"""Module contains class Node and class SinglyLinkedList"""


class Node:
    """class Node defines a node of a singly linked list by:

        - Private instance attribute: data
            - property def data(self): to retrieve it
            - property setter def data(self, value): to set it:
                - data must be an integer, otherwise raise a TypeError
                exception with the message data must be an integer
        - Private instance attribute: next_node
            - property def next_node(self): to retrieve it
            - property setter def next_node(self, value): to set it:
                - next_node can be None or must be a Node, otherwise raise a
                TypeError exception with the message next_node must be a Node
                object
    """
    def __init__(self, data, next_node=None):
        """Initializes an instance of the Node class"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if isinstance(value, int) is False:
            raise TypeError('data must be an integer')
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and isinstance(value, Node) is False:
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value


class SinglyLinkedList:
    """class SinglyLinkedList defines a singly linked list by:

        - Private instance attribute: head (no setter or getter)
        - Simple instantiation: def __init__(self)
        - It is printable
        - Public instance method: def sorted_insert(self, value)
    """
    def __init__(self):
        """Initialiazes an instance of the SinglyLinkedList class"""
        self.__head = None

    def __str__(self):
        """returns printable format for the SinglyLinkedList class"""
        ptr = self.__head
        res = ""
        delim = ""
        while ptr is not None:
            res += delim + str(ptr.data)
            delim = '\n'
            ptr = ptr.next_node
        return res

    def sorted_insert(self, value):
        """Inserts a new_node in the LinkedList in sorted order"""
        ptr = self.__head
        new_node = Node(value)
        if ptr is None:
            self.__head = new_node
        else:
            if ptr.data >= value:
                new_node.next_node = ptr
                self.__head = new_node
            else:
                while ptr.next_node is not None:
                    if value <= ptr.next_node.data:
                        new_node.next_node = ptr.next_node
                        ptr.next_node = new_node
                        return
                    ptr = ptr.next_node
                ptr.next_node = new_node
