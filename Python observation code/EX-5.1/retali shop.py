sum=0
unit=0
price=0
while True:
    items=input("Enter the item:")
    unit=int(input("Enter the unit:"))
    price=int(input("Enter the price:"))
    sum=sum+(unit*price)
    next=input("Do you want to continue(Y/N):")
    if next=="N":
        print("Total amount:",sum)
        break