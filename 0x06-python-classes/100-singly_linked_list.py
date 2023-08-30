#!/usr/bin/python3
'''
This module consists of two classes: a node and a singly linked list.
The module can be used to create a singly linked list of nodes
'''


class Node:
    '''Node will be an instance of a singly linked list and will act as
    the parent class in a singly linked list.
    '''
    def __init__(self, data, next_node):
        '''
        The init function fo class Node

        Args:
            data: the data to be stored in the node
            next_node: the next node in the singly linked list
        '''
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        '''
        Sets and gets the value of data

        Args:
            data (int): the data must be of type int

        Return:
            self.__data

        Raises:
            TypeError: If the data is not of type int
        '''
        return self.__data

    @data.setter
    def data(self, data):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = data

    @property
    def next_node(self):
        '''
        Sets and gets the value of next_node attribute

        Args:
            next_node: the next node which must be of type
            None of the Node

        Return:
            The next node

        Raises:
            TypeError: If value is not of type None or Node
        '''
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        if not (next_node is None or isinstance(next_node, Node)):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node


class SinglyLinkedList:
    '''
    This class uses the Node class.
    '''

    def __init__(self):
        '''
        The init method in this case does only initiate the head attribute

        Args:
            head (Node): the head of the singly linked list, defaults to None
        '''
        self.__head = None

    def __str__(self):
        '''
        The str method prints the contents of ths list
        '''
        arr = ""
        temp = self.__head
        while temp is not None:
            arr += f"{temp.data}\n"
            temp = temp.next_node
        return arr

    def sorted_insert(self, value):
        '''
        Function inserts a new Node into the correct sorted position in the
        singly linked list
        '''
        try:
            new = Node(value, None)
        except TypeError as err:
            print(f"{err}")
        else:
            temp = self.__head
            if temp is None or temp.data >= new.data:
                new.next_node = temp
                self.__head = new
            else:
                nxt_node = temp.next_node
                while nxt_node is not None and nxt_node.data < new.data:
                    temp = nxt_node
                    nxt_node = temp.next_node
                temp.next_node = new
                new.next_node = nxt_node if nxt_node is not None else None
