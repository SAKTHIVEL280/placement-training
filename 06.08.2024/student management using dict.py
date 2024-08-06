def menu():
    print("********************************************")
    print("1.Add student information")
    print("2.Update student information")
    print("3.View student information")
    print("4.Exit")
    print("********************************************")
    a=int(input("Enter your choice : "))
    if(a==1):
        addinfo()
    elif(a==2):
        upd()
    elif(a==3):
        view()
    elif(a==4):
        print("Exited !!")
    else:
        print("choose a valid option :)")
l={}
def addinfo():
    a=input("Enter the students name :")
    b=int(input("Enter the age of the student :"))
    l[a]=b
    print("_____________________________________________")
    print("Information added sucessfully")
    menu()
def upd():
    s=input("Enter the student name [to update] : ")
    for i in range(0,len(l)):
        if(s in l):
            print("Found the student")
            a=int(input("Enter the age to be updated : "))
            l[s]=a
            flag=1
            print("The age has been upgraded :)")
            print("_____________________________________________")
            break
        else:
            flag=0
    if(flag!=1):
        print("Not found :(")
        print("_____________________________________________")
    menu()
def view():
    r=input("Enter the students name : ")
    for i in range(0,len(l)):
        if(r in l):
            print("Student found :)")
            print(f"{r} {l[r]}")
            print("_____________________________________________")
            f=1
            break
        else:
            f=0
    if(f!=1):
        print("Student details not found :(")
        print("_____________________________________________")
    menu()
menu()

