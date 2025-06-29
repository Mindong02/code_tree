n = int(input())
cnt =0;
for a in range(n):
    if a % 2 ==0 or a % 3 ==0 or a % 5==0:
        continue
    else:
        cnt+=1

print(cnt)