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
            raise TypeError("width must be an integer")
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
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value   

    #creating getter and setter for x
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):#validation of x
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        elif value < 0: 
            raise ValueError("x must be >= 0")
        self.__x = value

    #creating getter and setter for y
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value): #validation of y
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        this method computes the area of rectangle
        area of rectangle is width * height
        """
        return self.width * self.height
    
    def display(self):
        """
        this method display the instance of a class  as #.
        loop will iterate over self.height as the column and self.width as the row
        since i'm using retutn statement, i will be using a variable result.
        """

        result = ""
        for _ in range(self.height):
            result += "#" * self.width + "\n"
        return result
    
if __name__ == "__main__":
    try:
        obj = Rectangle(1, 1)
        #print(obj.area())
        print(obj.display())
    except (TypeError, ValueError) as e:
        print(e)