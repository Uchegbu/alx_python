
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last_digit = abs(number) % 10
if number < 0:
    last_digit = -last_digit
if last_digit > 5 and last_digit != 0: 
    print("Last digit of {} is {} and is greater than 5".format(number,last_digit),end="\n")
elif last_digit == 0:
    print("Last digit of {} is {} and is 0".format(number,last_digit),end="\n")
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number,last_digit),end="\n")