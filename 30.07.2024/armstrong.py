x=int(input("Enter a number : "))
y=str(x)
t=0
for i in y:
    t+=int(i)**3
if x==t:
    print("It is an armstrong number :)")
else:
    print("Its not an armstrong number :(")
