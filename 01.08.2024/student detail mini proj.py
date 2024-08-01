def menu():
    print("**************************************************")
    print("1.Add student information")
    print("2.Update student information")
    print("3.View student information")
    print("4.To get avg of all students")
    print("5.Exit")
    print("**************************************************")
    a=int(input("Enter your choice : "))
    if(a==1):
        addinfo()
    elif(a==2):
        upd()
    elif(a==3):
        view()
    elif(a==4):
        avg()
    elif(a==5):
        print("Exited")
    else:
        print("choose a valid option :)")
l=[]
def addinfo():
    r=int(input("Enter the roll number of the student : "))
    a=input("Enter the students name :")
    b=int(input("Enter the age of the student :"))
    c=int(input("Enter the Mark of the student : "))
    lst1=[r,a,b,c]
    l.append(lst1)
    print("__________________________________________________")
    print("Information added sucessfully")
    menu()
def upd():
    s=int(input("Enter the students roll number [to update] : "))
    for i in range(0,len(l)):
        if(l[i][0]==s):
            print("__________________________________________________")
            print("Found the student")
            print("__________________________________________________")
            a=int(input("Enter the Mark to be updated : "))
            l[i][3]=a
            flag=1
            print("__________________________________________________")
            print("The Mark has been upgraded :)")
            break
        else:
            flag=0
    if(flag!=1):
        print("__________________________________________________")
        print("Not found :(")
    menu()
def view():
    r=int(input("Enter the students roll number : "))
    for i in range(0,len(l)):
        if(l[i][0]==r):
            print("__________________________________________________")
            print("Student found :)")
            print("__________________________________________________")
            print("Roll number : ",l[i][0])
            print("Name : ",l[i][1])
            print("Age : ",l[i][2])
            print("Mark : ",l[i][3])
            f=1
            break
        else:
            f=0
    if(f!=1):
        print("__________________________________________________")
        print("Student details not found :(")
        print("__________________________________________________")
    menu()
def avg():
    avg=0
    for i in range(0,len(l)):
        avg+=l[i][3]
        print("__________________________________________________")
    print("The average of all students is ",avg/len(l))
    print("__________________________________________________")
    menu()
menu()
    
        
        

