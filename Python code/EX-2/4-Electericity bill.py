ou=int(input("Enter old unit:"))
nu=int(input("Enter new unit:"))
unit=nu-ou
if(unit<=100):
    amount=0
elif(unit>100 and unit<=200):
    amount=(unit-100)*2.25
elif(unit>200 and unit<=400):
    amount=(100*2.25)+(unit-200)*4.5
elif(unit>400 and unit<=500):
    amount=(100*2.25)+(200*4.5)+(unit-400)*6
elif(unit>500 and unit<=600):
    amount=(100*2.25)+(200*4.5)+(100*6)+(unit-500)*8
elif(unit>600 and unit<=800):
    amount=(100*2.25)+(200*4.5)+(100*6)+(100*8)+(unit-600)*9
elif(unit>800 and unit<=1000):
    amount=(100*2.25)+(200*4.5)+(100*6)+(100*8)+(200*9)+(unit-800)*10
else:
    amount=(100*2.25)+(200*4.5)+(100*6)+(100*8)+(200*9)+(200*10)+(unit-1000)*11
print("The cost of the electric bill:",amount)