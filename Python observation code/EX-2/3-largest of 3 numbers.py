a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
c=int(input("Enter number 3:"))
if a>b and a>c:
    print("number 1 is greater")
elif b>a and b>c:
    print("number 2 is greater")
elif c>b and c>a:
    print("number 3 is greater")
else:
    print("All are equal")