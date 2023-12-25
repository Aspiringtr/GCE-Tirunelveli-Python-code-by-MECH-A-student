p=int(input("Enter the principle amount:"))
r=int(input("Interest rate percent:"))
t=int(input("Time in years:"))
n=int(input("Compound per year:"))
si=(p*r*t)/100
ci=p*((1+r/(100*n))**(n*t))-p
print("Simple intrest:",si)
print("Compound intrest",ci)