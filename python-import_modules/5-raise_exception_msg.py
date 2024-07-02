def raise_exception_msg(msg):
    try:
        raise NameError(msg)
    except NameError:
        print("c is fun")


if __name__ == "__main__":
     raise_exception_msg("hello")