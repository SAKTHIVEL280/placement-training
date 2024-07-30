def prime(a):
    for i in range(2,a):
        if a%i!=0:
            f=1
        else:
            f=0
    if f==1:
        print("prime")
    else:
        print("not prime")

a=int(input("Enter the number : "))
prime(a)
