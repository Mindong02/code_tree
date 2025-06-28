data = input().split()
text1  = str(data[0])
text2  = str(data[1])
a = len(text1)
b = len(text2)
if a<b:
    print(text2, b)
elif a==b:
    print("same")
else:
    print(text1, a)