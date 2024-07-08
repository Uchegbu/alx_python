def print_matrix_integer(matrix=[[]]):
    result = ""
    for row in matrix:
        for elem in row:
            result += "{:d} ".format(elem)
        result += "\n"
    return result

matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]


if __name__ == "__main__":
    print(print_matrix_integer(matrix))