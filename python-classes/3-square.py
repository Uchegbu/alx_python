class square:
  def __init__(self, size = 0): 
    """ using @property decorators to set getters and setters"""
    self.__size = size

    @property
    def size(self):
      return self.__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        if value <= 0:
            raise ValueError("Size must be greater than 0")
        self.__size

  def area(self):
    """this returns the area of the square """
    return self.__size **2