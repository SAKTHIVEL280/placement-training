a=input("Enter a sentence : ")
l=a.split()
for i in l:
    if len(i)%2==0:
        print(i,end=" ")
