#!/usr/bin/python3
"""
Singly linked list Module
"""


class Node:
    """
    Node class
    Attributes:
        data (int): the data stored in the node
        next_node (Node): a pointer to the next node
            in the linked list
    """
    def __init__(self, data, next_node=None):
        """
        Class initializer
        Args:
            data (int): the data stored in the node.
            next_node (Node): a pointer to the next node
        """
        self.data = data
        self.next_node = None

    @property
    def data(self):
        """
        Getter of the attribute data
        Returns:
            data: the stored data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter of the attribure data
        Args:
            value (int): the given data
        Raises:
            TypeError: if value is not integer
        """
        if not type(value) is int:
            raise TypeError("data must be integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Getter of the next_node
        Returns:
            next_node: a pointer to the next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter of the next_node
        Args:
            value (Node): a pointer to the next node
        Raises:
            TypeError: if value not node or None
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    """
    SiglyLinkedList defines the singly linked list
    Attributes:
        head (Node): a pointer to the singly linked list
    """
    def __init__(self):
        """
        Class initializer
        """
        self.__head = None

    def __str__(self):
        result = ""
        tmp = self.__head
        while tmp is not None:
            result += str(self.data)
            result += '\n'
            tmp = tmp.__next_node
        return result

    def sorted_insert(self, value):
        """
        Inserts new Node into the correct soeted position
        """
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