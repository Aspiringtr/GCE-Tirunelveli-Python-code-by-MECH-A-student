h=int(input("Enter the value of horse power:"))
v=int(input("Enter the value of voltage:"))
pf=int(input("Enter the value of power factor:"))
n=h*746
d=1.73*v*pf
current=n/d
print("The current in a 3phase AC circuit:",current)