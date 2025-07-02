arr_1 =[
    list(map(int, input().split()))
    for i in range(4)
]
cnt = 0
for i in range(4):
    for j in range(i+1):
        cnt += arr_1[i][j]


print(cnt)