s=set(input("Enter the components of automobile:").split())
print("Your sset is:",s)
print('SET OPERATIONS')
a=input("Enter a component to add:")
s.add(a)
print("set after adding:",s)
b=input("Enter a component to remove:")
if b in s:
    s.remove(b)
    print("Set after removing:",s)
else:
    print("The element is not in set")
c=input("Enter a component:")
if c in s:
    print("The component is present in set")
else:
    print("The element is not present in the set")
t=set(input("Enter component of automobile:").split())
g=set(input("Enter component of automobile:").split())
print("set1=",t)
print("set2=",g)
print("Intersection:",t.intersection(g))
print("Element in set 1 but not in set 2:",t-g)
print("Element in set 2 but not in set 1:",g-t)
print("Symmetric difference:",t^g)
print("union",t|g)