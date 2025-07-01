matrix = []

for i in range(3):
    row = list(map(int,input().split()))
    matrix.append(row)

for i in range(3):
    for j in range(3):
        matrix[i][j] *=3
        print(matrix[i][j], end=" ")
    print()