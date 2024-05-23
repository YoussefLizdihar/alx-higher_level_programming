#!/usr/bin/python3
"""This module defines a Node and a SinglyLinkedList class."""


class Node:
    """Represents a node in a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes the node with data and an optional next_node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of the node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list."""

    def __init__(self):
        """Initializes the singly linked list with an empty head."""
        self.__head = None

    def __str__(self):
        """Defines the string representation of the singly linked list."""
        result = []
        current = self.__head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """Inserts a new Node into the list in sorted order."""
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

