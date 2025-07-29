a = int(input())
sum=1
cnt=0
for i in range(1,101):
    sum+=i
    cnt=i
    if sum >= a:
        break


print(cnt)
