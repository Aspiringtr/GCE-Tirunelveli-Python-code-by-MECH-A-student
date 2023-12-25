s=input("Enter the string:")
c=input("Enter the character:")
count=0
for i in s:
    if i==c:
        count+=1
print(f"The character occured {count} times in a string")