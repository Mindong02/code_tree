a = int(input())

if a%4==0:
    print("true")
elif a%100==0:
    if a%400!=0:
        print("false")
    else:
        print("true")
else:
    print("false")