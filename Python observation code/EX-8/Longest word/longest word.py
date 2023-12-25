fi=open("E:/pythoncode/python/Python observation code/EX-8/Longest word/new.txt","r")
l=[]
for line in fi:
    words=line.split()
    for word in words:
        l.append(word)
r=len(l[0])
t=l[0]
for i in range(1,len(l)):
    if r < len(l[i]):
        r=len(l[i])
        t=l[i]
print("The longest word is ",t," and its length is ",r)