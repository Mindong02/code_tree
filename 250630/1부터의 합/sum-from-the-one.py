n = int(input())
cnt = 0
temp = 0
for i in range(1,n+1):
    if cnt <n:
        cnt+=i
        temp+=1
    else:
        break

print(temp)
