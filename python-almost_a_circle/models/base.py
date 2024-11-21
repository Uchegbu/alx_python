class Base:
    """
     Base class for all objects.
    This class provides a basic implementation of an object with an ID.
    """
    __nb_objects = 0  #private class attribute
    #creating a class constructor
    def __init__(self, id=None): #id is the Attribute.
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

if __name__ == "__main__":
    obj = Base(0)
    print(obj.id)