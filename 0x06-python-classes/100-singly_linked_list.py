#!/usr/bin/python3
"Creating a singly linked list node"

class Node:
    "Class Node"
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter"""
        if not isinstance(value, int):
            raise TypeError("data must begin with an integer")
        self.__data = value
    
    @property
    def next_node(self):
        """Getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object or None")
        self.__next_node = value

class SinglyLinkedList:
    """Class Singly Linked List"""
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        """Sorting insert"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Making it a string"""
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
