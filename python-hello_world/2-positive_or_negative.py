
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number > 0:
  print("{} is positive".format(number), end="\n")
elif number == 0:
  print("{} is zero".format(number), end="\n")
else:
  print("{} is negative".format(number), end="\n")