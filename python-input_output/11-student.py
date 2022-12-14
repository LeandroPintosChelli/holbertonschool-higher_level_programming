#!/usr/bin/python3
"""Creates a Student class."""


class Student:
    """Class that defines a student.
    Public attributes: first_name, last_name, age."""

    def __init__(self, first_name, last_name, age):
        """Initializes the Student instance."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation
        of a Student instance."""

        return self.__dict__

    def to_json(self, attrs=None):
        """Returns dictionary description of a Student instance:
        (list, dictionary, string)
        Return:
            only attribute names contained in this list
            Return entire dict if no attrs given
        """
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for x in attrs:
                if x in self.__dict__.keys():
                    dic[x] = self.__dict__[x]
            return dic

    def reload_from_json(self, json):
        """Replace all attributes of the Student.
        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for key, value in json.items():
            setattr(self, key, value)
