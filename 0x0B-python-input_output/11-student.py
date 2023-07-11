#!/usr/bin/python3
"""
Write a class Student that defines a student by:
Public instance attributes:
first_name
last_name
age
"""


class Student:
    """
    creating a class that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """ initializing the method"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieving a dictionary rep"""

        if type(attrs) == list and all(type(new) == str for new in attrs):
            return {new: getattr(self, new)
                    for new in attrs if hasattr(self, new)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replacing all attributes of the student"""

        for key, value in json.news():
            setattr(self, key, value)
