def common_elements(set_1, set_2):
    common_value = set_1.intersection(set_2)
    return common_value


if __name__ == "__main__":
    set_1 = {"java", "python", "css", "html"}
    set_2 = {"python", "css", "ruby"}
    print(common_elements(set_1, set_2))