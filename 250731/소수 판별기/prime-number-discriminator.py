a = int(input())
cnt = 0
for i in range(2,a+1,1):
    if a %i ==0:
        cnt+=1

if cnt>1:
    print("C")
else:
    print("P")