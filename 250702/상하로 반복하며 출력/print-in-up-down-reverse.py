a = int(input())
arr_1=[
    [0 for i in range(a)]
    for i in range(a)
]
for i in range(a):
    cnt=1
    if i % 2 != 0:    
        for j in range(a-1,-1,-1):
            arr_1[j][i]=cnt
            cnt+=1
    else:
        for j in range(a):
            arr_1[j][i]=cnt
            cnt+=1

for i in range(a):
    for j in range(a):
        print(arr_1[i][j],end="")
    print() 
        