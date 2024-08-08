a=input("Enter the elements of the list with spaces in between them : ")
b=a.split(" ")
temp1=[]
temp2=[]
for i in b:
    if i.islower():
        temp1.append(i)
    if i.isupper():
        temp2.append(i)
print("Lower :",temp1)
print("Upper :",temp2)
