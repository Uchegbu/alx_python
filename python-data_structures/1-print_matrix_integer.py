def print_matrix_integer(matrix=[[]]):
    result = ""
    for row in matrix:
        for elem in row:
            result += "{} ".format(elem)
        result += "\n"
    return result


if __name__ == "__main__":
    matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]
    
print(print_matrix_integer(matrix))