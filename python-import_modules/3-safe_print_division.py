def safe_print_division(a, b):
    try:
        result  =  a//b
    except ZeroDivisionError:
        result  = None
    finally:
        print("inside result: {}.0".format(result))
        print("{}/{} = {}.0".format(a,b, result))
    return result


if __name__ == "__main__":
    safe_print_division(10,2)