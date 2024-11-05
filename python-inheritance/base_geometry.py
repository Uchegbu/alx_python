"""
this python program is all about a class "BaseGeometry" with a public instance method that will raise an exception with the message 
area() is not implemented and another public instance method that validates integer.
"""

class BaseGeometry:
    """
   this class will contain two public instance method.
    """

    def __init__(self):
        pass


    def area(self): # raises an exception when called
        raise NotImplementedError("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        this method validate if value is an integer. i'm assuming that name is a string.value must be an integer and also greater than zero.
        if value is not an integer it raises typeerror exception and if value is less than zero or eqal to zero, it raises valuerror exception.
        """
    
        if not isinstance(name, str):
            raise TypeError("name must always be an string")
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
#creatint try-except block for area and integer validator
def area(obj):
    try:
        return(obj.area())
    except NotImplementedError as e:
        return(e)
    
def integer_validator(obj):
    try:
        return(obj.integer_validator("CAT", 0))
    except TypeError as e:
        return(e)
    except ValueError as e:
        return(e)
if __name__ == "__main__": 
#creating an instance of the class  
    obj = BaseGeometry()
    result1 = area(obj)
    result2 = integer_validator(obj)
    print(result1)
    print(result2)