a=int(input("Enter a number:"))
b=0
for i in range(2,a):
    if a%i==0:
        b=1
        break
if b==1:
    print(f"{a} is not a prime number")
else:
     print(f"{a} is a prime number")