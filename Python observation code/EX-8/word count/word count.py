fp=open("E:/pythoncode/python/Python observation code/EX-8/word count/newfile.txt","r")
count=0
for line in fp:
    words=line.split()
    count=count+len(words)
print("The total number of words is:",count)
fp.close()