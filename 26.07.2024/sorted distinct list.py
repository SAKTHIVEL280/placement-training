r=int(input("Enter how many elements r u going to enter : "))
l=[]
for i in range(r):
    a=int(input(f"Enter {i+1} element : "))
    l.append(a)
t=[]
for i in l:
    if i not in t:
        t.append(i)
print(sorted(t))
