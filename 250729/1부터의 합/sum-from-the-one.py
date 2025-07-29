a = int(input())
sum=1
cnt=0
for i in range(1,101):
    sum+=i
    cnt+=1
    if sum >= a:
        break


print(cnt)
