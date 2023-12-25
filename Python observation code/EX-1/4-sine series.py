theta=int(input("Enter the value of theta for sine series:"))
x=(theta*3.14)/180
sine_series=x-(x**3/(3*2))+(x**5/(5*4*3*2))
print(f"The sine series of sine {theta} is:",sine_series)