matrix = [[3,2,3],[1,3,1],[1,1,1]]

for i in range(3):
    for j in range(3):
        matrix[i][j] *=3
        print(matrix[i][j], end=" ")
    print()