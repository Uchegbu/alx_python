""" in this program,i will be validating the size of the square"""

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