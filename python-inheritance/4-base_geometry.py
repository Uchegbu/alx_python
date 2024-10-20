"""
this python program is all about a class "BaseGeometry" with a public instance method that will raise an exception with the message 
area() is not implemented. the try-except block will be use to catch the error when the def(area) of the BaseGeometry is called.
"""

class BaseGeometry:
    #in this class ther is no attribute but bthere ispublic instance method.
    def __init__(self,): #no parameters.
        pass

    def area(self): #when this function is called,it raises an error message instead of calculating area.
        raise NotImplementedError("area() is not implemented")

if __name__ == "__main__":     
#creating an instance of the class
    obj = BaseGeometry()
#creating a try-except exception block
def area(obj):
    try:
        return(obj.area())
    except NotImplementedError as e:
        return(e)
    
result = area(obj)
print(result)