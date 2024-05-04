
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
last_digit = abs(number) % 10
#print(last_digit)
if last_digit > 5: 
    print("last digit of {} is {} and is greater than 5".format(number,last_digit),end="\n")
elif last_digit == 0:
    print("last digit of {} is {} and is 0".format(number,last_digit),end="\n")
else:
    print("last digit of {} is {} and is less than 6 and not 0".format(number,last_digit),end="\n")