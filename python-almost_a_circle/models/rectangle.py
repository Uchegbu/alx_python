"""
Module for the Rectangle class.

This module contains the Rectangle class, which represents a rectangle
with attributes for width, height, x, and y.
"""

from models.base import Base

class Rectangle(Base):
    """
    contains four private instance attributes with its own public getters and setters
    """
    def __init__(self, width, height, x=0, y=0, id=None): 
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        

    #creating getter and setter for width
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        self.__width = value
    
    #creating getter and setter for height
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        self.__height = value

    #creating getter and setter for x
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        self.__x = value

    #creating getter and setter for y
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        self.__y = value

if __name__ == "__main__":
    obj = Rectangle(1, 3)
    obj.public_width = 1
    obj.public_height = 3
    obj.public_x = 2
    print(obj.public_x)