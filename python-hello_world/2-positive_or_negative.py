
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number > 0:
  print("{} is a positive number".format(number), end="\n")
elif number == 0:
  print("{} is zero".format(number), end="\n")
else:
  print("{} is a negative number".format(number), end="\n")