a=input("Enter the string : ")
c=0
v=["a","e","i","o","u","A","E","I","O","U"]
for i in range(len(a)):
    if a[i] in v:
        c+=1
print("Vowels :",c)
print("Consonents :",len(a)-c)
