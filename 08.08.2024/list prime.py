a=input("Enter the elements of the list with spaces in between them : ")
b=a.split(" ")
l=[]
temp=[]
for i in b:
    l.append(int(i))
for i in l:
    t=0
    if i!=2:
        for j in range(2,i):
            if i % j ==0:
                t=0
                break
            else:
                t=1
        if t==1:
            temp.append(i)
    else:
        temp.append(i)
print("original : ",l)
print("prime : ",temp)
