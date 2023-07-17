#!/usr/bin/python3
"""
a  class called base
"""
import json


class Base:
    """"
    a new class base for all the
    class in tthis project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        This initializes the new base
        of the project
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returning the JSON string rep
        of list_dictionaries
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        class that writes the JSON string rep
        of list_objs to a file
        """
        fname = cls.__name__ + ".json"
        with open(fname, "w", encoding="UTF-8") as newfile:
            if list_objs is None:
                newfile.write("[]")
            else:
                new_dic = [nw.to_dictionary() for nw in list_objs]
                newfile.write(Base.to_json_string(new_dic))

    @staticmethod
    def from_json_string(json_string):
        """
        returning the list of the JSON
        string rep json_string
        """

        if json_string is None:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returning an instance with all
        attributes already set
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                newinst = cls(1, 1)
            else:
                newinst = cls(1)
            newinst.update(**dictionary)
            return newinst

    @classmethod
    def load_from_file(cls):
        """
        returning a list of instances
        """
        fname = str(cls.__name__) + ".json"
        try:
            with open(fname, "r", encoding="UTF-8") as newfile:
                newinst = Base.from_json_string(newfile.read())
                return [cls.create(**dic) for dic in newinst]
        except IOError:
            return []
