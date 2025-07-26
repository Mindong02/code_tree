a = int(input())
cnt=0
b=1

for i in range(1,a+1):
    if i % 4==0:
        if i % 100 == 0:
            if i % 400 != 0:
                b=1
            else:
                cnt+=1
        else:
            cnt+=1


print(cnt) 