a,b = map(int, input().split())
c=a
print (c, end=" ")

for i in range(a,b+1):
    if i%2==0:
        c+=3
        if c<=b:
            print(c, end=" ")
    else:
        c*=2
        if c<=b:
            print(c, end=" ")