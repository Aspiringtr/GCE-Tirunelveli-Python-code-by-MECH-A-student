dic={}
n=int(input("Enter the total number of values:"))
for i in range(n):
    key=int(input("Enter a number:"))
    value=input("Enter a language:")
    dic[key]=value
print("Your dictionary is:",dic)
print("Dictionary Operator")
a=int(input("Enter a key value to access its value:"))
print("The value of the key is:",dic[a])
k=int(input("Enter a key value from the dictionary:"))
b=input("Enter a language to update:")
dic[k]=b
print("After updating:",dic)
p=int(input("Enter a new key value:"))
c=input("Enter a language to add:")
dic[p]=c
print("After adding:",c)
m=int(input("Enter a key value:"))
if m in dic:
    print("The key is in the dictionary ",m)
else:
    print("The key is not in the dictionary ",m)
print("Display items in the dictionary")
item=dic.items()
print(item)
print("Display values in the dictionary")
val=dic.values()
print(val)
print("Display keys in the dictionary")
key=dic.keys()
print(key)
print("Removing items in a dictionary")
r=int(input("Enter a key to remove:"))
if r in dic:
    dic.pop(r)
    print(dic)
else:
    print(r,"Is not found")