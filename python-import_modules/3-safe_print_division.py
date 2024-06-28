def safe_print_division(a, b):
    try:
        result  =  a/b
    except ZeroDivisionError:
        result  = None
    finally:
        print("inside result: {}".format(result))
        if result is not None:
            print("{} / {} = {}".format(a, b, result))
        else:
            print("{} / {} = None".format(a, b))



if __name__ == "__main__":
    safe_print_division(10,2)