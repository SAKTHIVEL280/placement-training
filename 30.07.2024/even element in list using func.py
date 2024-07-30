a=int(input("Enter how many elements u r going to enter : "))
l=[]
for i in range(a):
    x=int(input(f"Enter the number {i+1} : "))
    l.append(i)
def even_l(l):
    temp=[]
    for i in l:
        if i>=2:
            if i%2==0:
                temp.append(i)
    return temp
print(even_l(l))
