first=open("E:/pythoncode/python/Python observation code/EX-8/copy/oldfile.txt","r")
second=open("E:/pythoncode/python/Python observation code/EX-8/copy/newfile.txt","w")
for l in first:
    second.write(l)
print("The file has been copied successfully")
first.close()
second.close()
