name=input("Enter your name:")
computer=int(input("Enter your computer marks:"))
maths=int(input("Enter your maths marks:"))
physics=int(input("Enter your physics marks:"))
chemistry=int(input("Enter your chemistry marks:"))
english=int(input("Enter your english marks:"))
add=computer+maths+physics+chemistry+english
print("The Total marks:",add)
print(f"{name} got {add/5} %")