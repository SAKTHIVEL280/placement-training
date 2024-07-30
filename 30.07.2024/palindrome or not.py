a=input("Enter a string : ")
for i in range(len(a)):
    if a[i]==a[len(a)-1-i]:
        f=1
    else:
        f=0
        break
if f==1:
    print("Its a palindrome :)")
else:
    print("Its not a palindrome :( ")
