a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())

if a1==b1:
    if a1>a2:
        print("A")
    else:
        print("B")

elif a1>b1:
    print("A")

elif a1<b1:
    print("B")
else:
    a1+=1