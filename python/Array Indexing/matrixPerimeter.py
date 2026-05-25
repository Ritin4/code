def matrixPerimeter():
    matrix = [ 
        [1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]
    ]

    num_rows = len(matrix) 
    num_cols = len(matrix[0])
       
    for col in range(num_cols):
        print(matrix[0][col] , end=" ")
    print()

    for row in range(1, num_rows - 1):
        print(matrix[row][num_rows - 1] , end=" ")
    print()
    
    for col in range(num_cols - 1, -1, -1):
        print(matrix[num_cols - 1][col], end=" ")
    print()
    
    for row in range(num_rows-2, 0, -1):
        print(matrix[row][0], end=" ")
    print()

    

matrixPerimeter()