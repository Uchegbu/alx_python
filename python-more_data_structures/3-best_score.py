def best_score(a_dictionary):
    biggest_key = None
    biggest_value = float('-inf')
    for key, value in a_dictionary.items():
        if value > biggest_value:
            biggest_value = value
            biggest_key = key
    if biggest_key is None:
        return None
    return(biggest_key)
    
a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10} 


if __name__ == "__main__":
    print(best_score(a_dictionary))