def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for elem in row:
            print("{:d}".format(elem), end="")
        print("") 

matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]

if __name__ == "__main__":
    (print_matrix_integer(matrix))