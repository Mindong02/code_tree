a1,a2 = map(str, input().split())
b1,b2 = map(str, input().split())
c1,c2 = map(str, input().split())

a2=int(a2)
b2=int(b2)
c2=int(c2)

cnt=0

if a1=='Y' and a2>=37:
    cnt+=1
if b1=='Y' and b2>=37:
    cnt+=1
if c1=='Y' and c2>=37:
    cnt+=1

if cnt>=2:
    print("E")
else:
    print("N")
    
