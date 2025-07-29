a= int(input())
mul=1

for i in range(1,11,1):
    mul*=i
    if mul>=a:
        print(i)
        break