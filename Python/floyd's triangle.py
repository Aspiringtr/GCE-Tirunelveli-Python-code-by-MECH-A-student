n=int(input("Enter the number of rows:"))
k=1
for i in range(0,n):
    for j in range(0,i+1):
        print(k,end=" ")
        k+=1
    print()
