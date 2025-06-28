text = input()
result1 = text.replace(text[1],'a',1)
result2 = result1.replace(result1[-2],'a',1)
print(result2)