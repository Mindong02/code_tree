arr = []
cnt=0
for i in range(5):
    b = list(map(int, input().split()))
    arr.extend(b)

for i in range(5):
    if arr[i] % 2==0:
        cnt+=1

print(cnt)