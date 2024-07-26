s=input("Enter the string : ")
x=input("Which character u need to count : ")
c=0
for i in range(len(s)):
    if s[i]==x:
        c+=1
print("count : ",c)
