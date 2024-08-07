a=int(input("Enter the rows : "))
for i in range(a):
    for j in range(a-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end= " " )
    print()
