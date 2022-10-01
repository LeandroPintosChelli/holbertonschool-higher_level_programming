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

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
