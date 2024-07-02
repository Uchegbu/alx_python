def raise_exception_msg(message=""):
    try:
        raise NameError("hello")
    except NameError:
        print("c is fun")


if __name__ == "__main__":
     raise_exception_msg("hello")