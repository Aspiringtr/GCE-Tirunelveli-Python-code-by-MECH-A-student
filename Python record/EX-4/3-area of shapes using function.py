def rectangle():
    l=int(input("Input the length:"))
    b=int(input("Input the breadth:"))
    return l*b
def circle():
    r=int(input("Input the radius:"))
    return r*r
def triangle():
    b=int(input("Input the base:"))
    h=int(input("Input the height:"))
    return b*h/2
def continue_():
    cont=input("Input 'YES' to continue and 'NO' to quit:")
    if cont.upper()=='YES':
        main_func()
def main_func():
    print("rectangle,circle and tringle")
    operation=input("Input the shape:")
    if operation.upper()=="RECTANGLE":
        print(f"Area of rectangle is {rectangle()}")
        continue_()
    elif operation.upper()=="CIRCLE":
        print(f"Area of circle is {circle()}")
        continue_()
    elif operation.upper()=="TRIANGLE":
        print(f"Area of triangle is {triangle()}")   
        continue_()     
    else:
        print("No such operation")
        continue_()
main_func()
