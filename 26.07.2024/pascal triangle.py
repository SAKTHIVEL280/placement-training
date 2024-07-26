n=int(input("Enter a number : "))
for i in range(n):
    c=[1]
    for j in range(1,i+1):
        p=c[-1]
        n=p*(i-j+1)//j
        c.append(n)
    print(*c)
