def no_c(my_string):
    result = ""
    for char in my_string:
        if char.lower() != 'c':
            result += char
    return result


if __name__ == "__main__":
    print(no_c())