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
        try:
            self.width = width
            self.height = height
            self.x = x
            self.y = y
        except TypeError as e:
            raise TypeError(e)
        except ValueError as e:
            raise ValueError(e)

        

    #creating getter and setter for width
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, value):
        if not isinstance(value, int):#validation for width
            raise TypeError("width must be a integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    #creating getter and setter for height
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance(value, int):#validation of height
            raise TypeError("height must be a integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value   

    #creating getter and setter for x
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        if value < 0: #validation of x
            raise ValueError("x must be >= 0")
        self.__x = value

    #creating getter and setter for y
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value): #validation of y
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

if __name__ == "__main__":
    try:
        obj = Rectangle(0, 3,)
        print(obj.width)
    except (TypeError, ValueError) as e:
        print(e)