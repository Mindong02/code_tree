a=int(input())

for i in range(1,a+1):
    for j in range(1,a+1):
        if j <= a-1:
            print(f"{i} * {j} = {i*j}", end=", ")
        else:
            print(f"{i} * {j} = {i*j} ")
print()