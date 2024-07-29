def menu():
    print("***************************************************************")
    print("1.add\n2.sub\n3.multiply\n4.div\n5.exit :)")
    a=int(input("Enter the option : "))
    x=int(input("Enter the 1st number : "))
    y=int(input("Enter the 2nd number : "))
    if a==1:
        print(f"The addition of {x} and {y} is {x+y}")
        menu()
    elif a==2:
        print(f"The subtraction of {x} and {y} is {x-y}")
        menu()
    elif a==3:
        print(f"The multiplication of {x} and {y} is {x*y}")
        menu()
    elif a==4:
        print(f"The division of {x} and {y} is {x/y}")
        menu()
    elif a==5:
        print("closed !! ")
        
menu()
