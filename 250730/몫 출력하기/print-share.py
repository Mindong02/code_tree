cnt=0
while(1):
    a = int(input())
    if a%2==0:
        cnt+=1
        print(a//2)
    
    if cnt==3:
        break