def printDiagonal():
    matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
    ]

    #length of matrix
    n = len(matrix)
    print(n)

    #looping through diagonal
    for i in range(n):
        print(matrix[i][i], end=" ")
    print()

printDiagonal()