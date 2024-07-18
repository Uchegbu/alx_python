def square_matrix_simple(matrix=[]):
    if not matrix or not matrix[0]:
        return[]
    squared_matrix = []
    for row in matrix:
        squared_row = []
        for elem in row:
            squared_row.append(elem**2)
        squared_matrix.append(squared_row)
    return squared_matrix 

matrix = [
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5]
]


if __name__ == "__main__":
    print(square_matrix_simple(matrix))