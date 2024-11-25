from base import Base
class Rectangle(Base):
    """
    contains four private instance attributes with its own public getters and setters
    """
    def __init__(self, width, height, x=0, y=0, id=None): 
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    #creating getter and setter for width
    @property
    def public_width(self):
        return self.__width
    @public_width.setter
    def public_width(self, value):
        self.__width = value
    
    #creating getter and setter for height
    @property
    def public_height(self):
        return self.__height
    @public_height.setter
    def public_height(self, value):
        self.__height = value

    #creating getter and setter for height
    @property
    def public_x(self):
        return self.__x
    @public_x.setter
    def public_x(self, value):
        self.__x = value

    #creating getter and setter for height
    @property
    def public_y(self):
        return self.__y
    @public_y.setter
    def public_y(self, value):
        self.__y = value

if __name__ == "__main__":
    obj = Rectangle(1, 3)
    obj.public_width = 1
    obj.public_height = 3
    obj.public_x = 2
    print(obj.public_x)