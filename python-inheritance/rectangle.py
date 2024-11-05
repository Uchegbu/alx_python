"""
This python script will be inheriting from the class BaseGeometry which i will be importing as module. this script will have attribute i.e 
width and height and no methods.The width and height will be validated as whether be postive integer by integer_validator from the BaseGeometry.
note: width and height are private attribute.
"""
from base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        try:
            super().integer_validator("width", width)
            super().integer_validator("height", height)
            self.__width = width
            self.__height = height
        except ValueError as e:
            raise ValueError("invalid rectangle dimension:{}".format(e))
if __name__ == "__main__":  
    try:
        obj = Rectangle(4,9)
    except ValueError as e:
        print(e)
    else: #when the integers are positive, else statement print.
        print(obj._Rectangle__width)
        print(obj._Rectangle__height)