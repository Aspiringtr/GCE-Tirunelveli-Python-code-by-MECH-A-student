name=input("Enter your name:")
computer=int(input("Enter your computer marks:"))
maths=int(input("Enter your maths marks:"))
physics=int(input("Enter your physics marks:"))
chemistry=int(input("Enter your chemistry marks:"))
english=int(input("Enter your english marks:"))
p=(computer+maths+physics+chemistry+english)/5
if(p>=90 and p<=100):
    print(f"{name} got A grade")
elif(p>=70 and p<=89):
    print(f"{name} got B grade")
elif(p>=50 and p<=69):
    print(f"{name} got C grade")
elif(p>=35 and p<=49):
    print(f"{name} got D grade")
else:
    print(f"{name} got F grade")