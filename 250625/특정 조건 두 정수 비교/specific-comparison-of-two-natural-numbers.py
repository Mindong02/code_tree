temp = input()
arr = temp.split()
a=int(arr[0])
b=int(arr[1])
if a<b:
    print("1")
elif a>=b:
    print("0")
elif a==b:
    print("1")
else:
    print("0")