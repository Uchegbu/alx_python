"""
this script write a function that returns true if the object is an instance of,or if the object
is an instance of a class that inherited from, the specified class,otherwise false.
"""

class Animal:
    """"
    this is the parent class
    """
    def __init__(self): #no parameter pass
        pass

class a_class(Animal):
    """
    this class is a subclass of Animal and will serve as the specified class
    """
    def __init__(self): #no parameter passed
        pass

class Cat(a_class):
    """
    this is subclass of Dog and it is inheriting from dog
    """
    def __init__(self): #no parameter is passed
        pass

"""
creating a funcion that return true when is an instance or inheriting from the specifird class
"""
def is_kind_of_class(obj,a_class):
    return isinstance(obj,a_class)

if __name__ == "__main__":
#creating an instance of Dog
  obj = a_class()
  my_cat = Cat()

print(is_kind_of_class(obj,a_class))