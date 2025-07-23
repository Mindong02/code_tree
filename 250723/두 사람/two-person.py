a1,a2= map(str,input().split())
b1,b2= map(str,input().split())
a1 = int(a1)
b1 = int(b1)
if a1>=19 or b1>=19:
    if a2 =='M' or b2 == 'M':
        print("1")
    else:
        print("0")