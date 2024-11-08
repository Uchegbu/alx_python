"""
This script is a full rectangle. This python script will be inheriting from the class BaseGeometry which i will be importing as module. 
this script will have attribute i.e width and height and methods.The width and height will be validated as whether be postive integer
by integer_validator from the BaseGeometry.note: width and height are private attribute. 
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

    def __str__(self) -> str:
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        return self.__width * self.__height
    
if __name__ == "__main__":  
    try: 
        obj = Rectangle(7,0)
        print(obj)
        print(obj.area())
    except ValueError as e:
        print(e)