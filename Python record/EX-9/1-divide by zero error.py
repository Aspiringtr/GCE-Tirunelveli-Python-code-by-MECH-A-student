try:
    a=int(input("Enter the numerator:"))
    b=int(input("Enter the denominator:"))
    c=a/b
    print("The quotient is:",c)
except:
    print("Can't divide by zero")
else:
    print("Division performed successfully")

