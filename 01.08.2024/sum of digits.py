a=333
b=str(a)
for i in range(0,len(b)):
    a=int(a%10)+int(a/10)
print(a)

