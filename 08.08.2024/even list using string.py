a=input("Enter the elements of the list with spaces in between them : ")
b=a.split(" ")
l=[]
temp=[]
for i in b:
    l.append(int(i))
for i in l:
    if i % 2 ==0:
        temp.append(i)
print("original : ",l)
print("Even nums : ",temp)
