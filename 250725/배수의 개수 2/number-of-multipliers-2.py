arr = []
cnt = 0
for i in range(10):
    b = list(map(int, input().split()))
    arr.extend(b)

for i in range(10):
    if arr[i] % 2==1:
        cnt+=1

print(cnt)

