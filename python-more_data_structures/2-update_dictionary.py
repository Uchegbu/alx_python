def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary[key] = value
    return a_dictionary

a_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

if __name__ == "__main__":
   print(update_dictionary(a_dictionary, 'b', 4))