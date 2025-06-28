a, b, c = map(int, input().split())

if a>b:
    if c<a:
        if b<c:
            print(c)
        else:
            print(b)
    else:
        print(a)
else: # a<b -> b<c or c<b
    if b<c:
        print(b)
    else:
        if a<c:
            print(c)
        else:
            print(a)
