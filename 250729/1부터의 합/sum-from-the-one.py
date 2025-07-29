a = int(input())
sum=1
cnt=1
for i in range(1,101):
    sum+=i
    cnt+=1
    if sum >= a:
        break

cnt-=1
print(cnt)
