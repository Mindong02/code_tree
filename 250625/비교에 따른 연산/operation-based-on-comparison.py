arr = input()
split_arr = arr.split()
a = int(split_arr[0])
b = int(split_arr[1])

if a > b:
    print(a*b)
else:
    print(b//a)