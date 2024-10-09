"""
this script will create A function that returns true if the object is exactly an instance of the specified class and othwerwise false,i.e i'm working on inheritance
"""

class Animal:
    """
    this class "animal" will serve as the parent class or super class. 
    """
    def __init__(self): # no parameter is passed,it is empty.
        pass

class a_class(Animal):
    """
    this class "a_class" is the subclass of "Animal",a_class is inheriting from animal.
    """
    def __init__(self): # no parameter is passed,it is empty.
        pass

"""
a function that return true if an object is exactly the same of a class and false otherwise.
"""
def is_same_class(obj, a_class):
    return type(obj) == a_class

if __name__ == "__main__":
#creating an instance of the class a_class
   obj = a_class()

print(is_same_class(obj, a_class))