a, b = map(int, input().split())
cnt1=0
cnt=0

for j in range(a,b+1): # 약수 구하기 위해서 j를 a부터 b+1까지 차츰 올림
    for t in range(1,j+1): # j가 a 일때 t는 1부터 j까지 1씩 증가 이때 j가 t에 대해서 약수를 찾기 시작 
        if j % t == 0:
            cnt += 1
    if cnt == 3:
        cnt1 += 1
    cnt=0
print(cnt1)