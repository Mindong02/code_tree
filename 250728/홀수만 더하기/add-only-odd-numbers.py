a = int(input())
arr = []
sum=0

for i in range(a):
    b = list(map(int, input().split()))
    arr.append(b)

for i in range(a):
    if arr[i]%2==1 and arr[i]%3==0:
        sum+=arr[i]


print(sum)