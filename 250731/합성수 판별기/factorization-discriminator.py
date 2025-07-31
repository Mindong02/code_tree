a = int(input())
cnt=0
for i in range(2,a,1):
    if a%i==0:
        cnt+=1

if cnt>0:
    print("C")
else:
    print("N")