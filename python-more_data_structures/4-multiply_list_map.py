def multiply_list_map(my_list=[], number=0):
    return (list(map(lambda x:x*number,my_list)))
my_list = [2, 3, 4, 5]
number = 0

if __name__ == "__main__":
    print(multiply_list_map(my_list,number))