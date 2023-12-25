fruits=input("Enter the fruits:").split()
time=int(input(f"Enter the circulation number from 0 to {len(fruits)}:"))
for i in range(1,time+1):
    a=fruits[i:]+fruits[:i]
    print("After circulation:",a)