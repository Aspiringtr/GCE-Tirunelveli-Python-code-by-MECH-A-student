try:
    a=int(input("Enter your age:"))
    if(a>=18):
        print("Eligiable to vote")
    else:
        print("Not eligiable to vote")
except:
    print("Enter a valid age")