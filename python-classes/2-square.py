class square:
  def __init__(self, size = 0): 
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square (default=0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
      """

        if not isinstance(size, int):
          raise TypeError("size must be an integer")
        if size <= 0:
          raise ValueError("size must be >= 0")

        self.__size = size
  
  def area(self):
    """this returns the area of the square """
    return self.__size **2
  
#s1 = square(5)

#print("area of square is {}".format(s1.area()))