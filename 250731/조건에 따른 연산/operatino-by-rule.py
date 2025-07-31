a = int(input())
cnt=0
while(1):
    if a%2==0:
        a=3*a+1
        cnt+=1
    elif a%2==1:
        a=2*a+2
        cnt+=1
    if a>=1000:
        print(cnt)
        break