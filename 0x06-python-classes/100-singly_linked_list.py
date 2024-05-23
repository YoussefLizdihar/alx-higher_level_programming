#!/usr/bin/python3
"""this is a Node Class """


class Node:

    """
    Node class
    Attributes:
        next_node: a pointer to the next node
    """

    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = None

    # size property
    @property
    def date(self):
        return self.__data
    # size setter with conditions
    @data.setter
    def data(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value != Node:
            raise TypeError("next_node must be a Node object")
        self.__position = value



class SinglyLinkedList:
    """
    SinglyLinkedList class
    Attributes:
        head : a pointer
    """
    def __int__(self):
        self.__head == None:
        
    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
        else:
            new_node = Node(value)
            tmp = self.__head
            while tmp is not None:
                if tmp.__next_node is None:
                    tmp.__next_node = new_node
                    new_node.__next_node = None
                if new_node.__data < tmp.__next_node.__data:
                    new_node.__next_node = tmp.__next_node
                    tmp.__next_node = new_node
                tmp = tmp.__next_node
