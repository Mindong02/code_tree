cnt = 0
b=1
a = int(input())

while(1):
    if a%2==0:
        a=a//2
        cnt+=1
    elif a%2==1 and a!=1:
        a=3*a+1
        cnt+=1
    else:
        b=1
    if a==1:
        print(cnt)
        break