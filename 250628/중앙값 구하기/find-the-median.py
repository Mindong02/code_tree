a, b, c = map(int, input().split())

if a>b:
    if c<a:
        print(c)
    else:
        print(a)
else: # a<b -> b<c or c<b
    if b<c:
        print(b)
    else:
        print(c)
