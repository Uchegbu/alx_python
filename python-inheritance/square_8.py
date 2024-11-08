"""
A class that inherits from Rectangle
instantiation with size
size = positive integers and validated by integer_validator
size is private,no mgetters and setters
are() must be 
note i will be importing Rectangle as module.
"""

from rectangle_7 import Rectangle

class Square(Rectangle):
    def __init__(self, size):
        try:
            super().integer_validator("size", size)
            self.__size = size
        except ValueError as e:
            raise ValueError("invalid square dimensions:{}".format(e))

    def __str__(self) -> str:
        return "[Square] {}*2".format(self.__size)  
    
    def area(self):
        return self.__size*2
try:
    obj = Square(8)
    print(obj)
    print(obj.area())
except ValueError as e:
    print(e)