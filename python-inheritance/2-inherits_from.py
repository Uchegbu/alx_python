"""
write a function that returns true if the object is an instance of a class that inherited(directly or indirectly)
from the specified class; otherwise false
"""

class Animal:
    """
    this class serve as the parent class
    """
    def __init__(self): # no parameter given.
        pass

class Mammal(Animal):
    """
    this class inherits directly from the parent class.
    """
    def __init__(self): # no parameter given.
        pass

class a_class(Mammal):
    """
    this class inherits directly from mammal and indirectly from animal.
    """
    def __init__(self): #no parameter pass.
        pass

class Cat(Mammal):
    """"
    this class inherits from mammal directly and indirectly from animal.
    note, it is not inheriting from a_class.
    """
    def __init__(self): #no parameter given.
        pass

"""
using "isstance()" function to create a function that returns true if the object is an instance of a class that inherited
(directly or indirectly)from the specified class; otherwise false
"""

def inherits_from(obj,a_class):
    return isinstance(obj, a_class)

if __name__ == "__main__":
#creating an instance of a_class and Cat.
   obj = a_class()
   my_cat = Cat()

print(inherits_from(obj, a_class))
print(inherits_from(obj, Animal))
print(inherits_from(obj, Mammal))
print(inherits_from(obj, Cat))
print(inherits_from(my_cat, a_class))
print(inherits_from(my_cat, Cat))
print(inherits_from(my_cat, Mammal))
print(inherits_from(my_cat, Animal))