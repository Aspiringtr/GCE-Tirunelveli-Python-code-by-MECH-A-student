try:
    inter=float(input("Enter your Internal marks out of 200:"))
    semes=float(input("Enter your semester marks out of 100:"))
    a=(inter/200)*40
    b=(semes/100)*60
    tot=a+b
    print("Your mark is:",tot)
    if(91<=tot<=100):
        print("Grade is outstanding")
    elif(81<=tot<=90):
        print("Grade is A+")
    elif(71<=tot<=80):
        print("Grade is A")
    elif(61<=tot<=70):
        print("Grade is B+")
    elif(50<=tot<=60):
        print("Grade is B")
    else:
        print("Arrear")
except:
    print("Enter a valid mark")