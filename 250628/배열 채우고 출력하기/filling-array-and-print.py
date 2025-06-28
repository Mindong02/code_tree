char = list(map(str,input().split()))
n = len(char)
char.reverse()
for i in range(n):
    print(char[i], end="")