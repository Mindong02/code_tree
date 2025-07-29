a = int(input())
sum=1

for i in range(1,101):
    sum+=i
    if sum >= a:
        sum-=i
        break

print(sum)
