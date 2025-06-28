a,b = map(int, input().split())
arr = []
arr.append(a)
arr.append(b)

for i in range(8):
    new= arr[i+1] + arr[i]
    arr.append(new)

for i in range(10):
    arr[i] %= 10
    print(arr[i], end= " ")