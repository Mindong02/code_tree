arr_1=[
    list(map(int, input().split()))
    for _ in range(4)
]

total=0

for i in range(4):
    for j in range(4):
        total+= arr_1[i][j]
    print(total)
    total=0