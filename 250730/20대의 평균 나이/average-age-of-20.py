cnt=0
sum1=0

while(1):
    a = int(input())
    if a>=30 or a<=19:
        print(f'{sum1/cnt:.2f}')
        break
    cnt+=1
    sum1+=a
