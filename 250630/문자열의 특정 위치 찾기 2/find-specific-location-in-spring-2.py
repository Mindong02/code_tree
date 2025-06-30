n = str(input())

a = ['apple', 'banana', 'grape', 'blueberry', 'orange']
b = list()

cnt=0

for i in range(5):
    if a[i][2] == n or a[i][3] == n:
        cnt +=1
        b.append(a[i])

leng = len(b)

for i in range(leng):
    print(b[i])

print(cnt)