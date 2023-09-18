#!/usr/bin/python3
'''This file describes the Base class of the geometric classes
'''
import json
from inspect import getargspec


class Base:
    '''This class describes methods can be used to initialise objects
    of child classes. As the root class, it also provides interfaces
    for creating objects from json files and strings. It also has
    methods that can be used with cls files.

    Attributes:
        __nb_objects (int): a unique identifier of created instances
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''mainly sets the value of id

        Note:
            This object is expected to be called by its children
            only.
        Args:
            id (int): uniquely identifies a specific instance
        '''
        if id is None:
            Base.__nb_objects += 1
        self.id = id if id is not None else Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''generates a string representation of json dictionaries

        Args:
            list_dictionaries (list): a list of json dictionaries

        Returns:
            an empty list if list_dictionaries is None, otherwise,
            it returns a json string representation.
        '''
        res = "[]"
        if list_dictionaries is not None:
            res = json.dumps(list_dictionaries)
        return res

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to
        a file. The name of the file written to is the class name
        of the object calling this method.

        Args:
            list_objs: the JSON string representation of JSON objects

        Returns:
            None.
        '''
        res = "[]"
        file_name = f"{cls.__name__}.json"
        if list_objs is not None:
            item = map(lambda el: el.to_dictionary(), list_objs)
            res = Base.to_json_string(list(item))
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(res)

    @classmethod
    def from_json_string(cls, json_string):
        '''returns a list or directory from a JSON string

        Args:
            json_string (str): string representation of JSON objects
        Returns:
            dictionaries or list of dictionaries parsed from JSON
            objects.
        '''
        res = []
        if json_string is not None:
            res = json.loads(json_string)
        return res

    @classmethod
    def create(cls, **dictionary):
        '''creates an instance of the class or its children from a
        dictionary.

        Args:
            dictionary (dict): dictionary representation of the object to
            be initialised
        Returns:
            new object of type cls
        '''
        defaults = getargspec(cls.__init__).defaults
        allpars = getargspec(cls.__init__).args
        vals = []
        for i in range(len(defaults), len(allpars)):
            vals.append(1)
        print(vals)
        dummy = cls(*vals)
        dummy.update(dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances from the loaded json file. It
        assumes an existing file called filename in the current directory

        Returns:
            empty list if the file does not exist. Otherwise, the list of
            created instances
        '''
        file_name = f"{cls.__name__}.json"
        instances = []
        res = []
        try:
            with open(file_name, "w", encoding="utf-8") as f:
                instances = json.load(f)
        except FileNotFoundError as e:
            return res
