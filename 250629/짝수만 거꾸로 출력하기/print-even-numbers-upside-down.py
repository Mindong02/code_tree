a = int(input())

a1 = list(map(int, input().split()))

for i in range(a-1, -1, -1):
    if a1[i] % 2 == 0:
        print(a1[i], end = " ")
