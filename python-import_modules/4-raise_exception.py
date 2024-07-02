def raise_exception():
    try:
        "heelo" + 5
    except TypeError:
        print("exception has been raised")


if __name__ == "__main__":
    raise_exception()