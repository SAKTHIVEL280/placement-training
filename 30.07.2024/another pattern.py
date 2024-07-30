a=int(input("Enter the range : "))
for i in range(1,a+1):
    for j in range(i):
        print("*",end=" ")
    print("")
for i in range(a):
    for j in range(a-i):
        print("*",end=" ")
    print("")
