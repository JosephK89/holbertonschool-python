#!/usr/bin/python3


class Node:
    """node
    """
    def __init__(self, data, next_node=None):
        """initialization of the node 
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter fct
        """
        return self.__data

    @data.setter
    def data(self, value):
        """setter fct
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter fct
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter fct
        """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __str__(self):
        """str
        """
        return str(self.__data)


class SinglyLinkedList:
    """linked list class
    """
    def __init__(self):
        """initialization of the list
        """
        self.__head = None

    def sorted_insert(self, value):
        """ insert fct
        """
        new = Node(value)
        tmp = self.__head
        if tmp is None or tmp.data >= value:
            if tmp:
                new.next_node = tmp
            self.__head = new
            return
        while tmp.next_node is not None:
            if tmp.next_node.data >= value:
                break
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new

    def __str__(self):
        """str
        """
        string = ""
        tmp = self.__head
        while tmp is not None:
            string += str(tmp)
            if tmp.next_node is not None:
                string += "\n"
            tmp = tmp.next_node
        return string
