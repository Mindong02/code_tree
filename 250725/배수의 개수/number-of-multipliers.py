arr=[]
cnt3 = 0
cnt5=0
for i in range(10):
    b = list(map(int, input().split()))
    arr.extend(b)
    if arr[i] % 3 == 0:
        cnt3+=1
    if arr[i] % 5 == 0:
        cnt5+=1

print(cnt3, cnt5, end=" ")