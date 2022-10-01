#!/usr/bin/python3
"""Create a Rectangle class, inheriting from Base."""

import json
from models.base import Base


class Rectangle(Base):
    """Class rectangle that Inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance.
             Args:
            - __width: width
            - __height: height
            - __x: position
            - __y: position
            - id: id
            """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves the width attribute."""

        return self.__width

    @property
    def height(self):
        """Retrieves the height attribute."""

        return self.__height

    @property
    def x(self):
        """Retrieves the x attribute."""

        return self.__x

    @property
    def y(self):
        """Retrieves the y attribute."""

        return self.__y
