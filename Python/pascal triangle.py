n=int(input("Enter the number of rows:"))
d=1
for i in range (0,n+1):
    for j in range(0,n-i):
        print(" ",end="")
    for k in range(0,i):
        if(i==0 or k==0):
            d=1
        else:
            d=d*(i-k)//k
        print(d,end=' ')
    print()