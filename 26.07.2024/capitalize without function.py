s=input("Enter the sentence : ")
l=s.split()
t=[]
for i in l:
        if i[0].islower():
            t.append(i[0].upper()+i[1:])
        else:
            t.append(i)
print(" ".join(t))
