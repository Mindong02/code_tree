N = int(input())
cnt = 100-N+1

for i in range(cnt):
    if N>=90:
        print("A", end=" ")
    elif N>=80:
        print("B", end=" ")
    elif N>=70:
        print("C", end=" ")
    elif N>=60:
        print("D", end=" ")
    else:
        print("F", end=" ")
    N+=1
    

