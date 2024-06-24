import sys

def print_arguments():
    argv = sys.argv
    num_args = len(argv) - 1
    if num_args == 0:
        return "{} arguments.".format(num_args)
    elif num_args == 1:
        return "{} argument:".format(num_args) + "\n" + "{}: {}".format(1, argv[1])
    else:
        result = "{} arguments:".format(num_args)  + "\n"
        for i in range(num_args):
            result  += "{}:{}".format(i + 1, argv[i + 1]) + " " + "\n"
        return result    

if __name__ == "__main__":
    print(print_arguments())