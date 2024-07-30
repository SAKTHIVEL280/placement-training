a=int(input("Enter a number :"))
t=0
for i in range(1,a):
    if a%i==0:
        t+=i
if a==t:
    print("Its a perfect number :)")
else:
    print("Its not a perfect number :(")
