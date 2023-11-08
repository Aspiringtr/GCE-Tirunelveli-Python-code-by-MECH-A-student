def max (lis):
    max=lis[0]
    for i in lis:
        if i > max:
            max=i
    return max
l=list(map(int,input("Enter the elements:").split()))
print("Maximum number in a list:",max(l))