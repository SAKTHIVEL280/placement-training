s=input("Enter the sentence : ")
l=s.split()
lo=0
u=0
for i in l:
    for j in range(len(i)):
        if i[j].isupper():
            u+=1
        if i[j].islower():
            lo+=1
print("Upper case :",u,"\nLower case :",lo)
