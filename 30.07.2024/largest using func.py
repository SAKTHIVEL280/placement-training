def largest():
    x=int(input("Enter the 1st : "))
    y=int(input("Enter the 2nd : "))
    z=int(input("Enter the 3rd : "))
    if x>y and x>z:
        print("larger number is x :",x)
    if y>x and y>z:
        print("larger number is y :",y)
    if z>y and z>x:
        print("larger number is z :",z)

print("we r going to find the largest of number of 3 inputs")
largest()
