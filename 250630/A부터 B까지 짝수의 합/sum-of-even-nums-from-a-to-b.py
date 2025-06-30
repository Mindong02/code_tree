a,b = map(int, input().split())
cnt = 0

for i in range(a,b):
    if i % 2 ==0:
        cnt+=i
    else:
        continue
print(cnt)
        