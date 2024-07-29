a=input("Enter a string : ")
s=""
for i in a:
    if i not in s:
        s+=i
print(s)
