def menu():
    print("AREA")
    print("1.rectangle\n2.square\n3.triangle\n4.circle\n5.Exit!!")
    n=int(input("Enter the option : "))
    if n==1:
        rec()
    if n==2:
        sq()
    if n==3:
        tri()
    if n==4:
        ci()
    if n==5:
        print("Exit !! ")
    else:
        print("pls Enter a valid option :)")

def rec():
    a=int(input("Enter the length : "))
    b=int(input("Enter the breadth : "))
    print("area : ",a*b)
    menu()
def sq():
    a=int(input("Enter the length : "))
    print("area : ",a**2)
    menu()
def tri():
    a=int(input("Enter the base : "))
    b=int(input("Enter the height : "))
    print("area : ",0.5*(a*b))
    menu()
def ci():
    a=int(input("Enter the radius : "))
    print("Area : ",3.14*r*r)
    menu()
menu()
