a = int(input())
arr=[]
for i in range(a):
    b = list(map(int, input().split()))
    arr.extend(b)

for i in range(a):
    if arr[i]%2==1 and arr[i]%3==0:
        print(arr[i]) 