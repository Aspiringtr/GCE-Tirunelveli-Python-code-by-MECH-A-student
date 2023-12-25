from matplotlib import pyplot as plt
marks=(18.35,45.37,83.9,55.78,99.23)
grades=(0,25,50,75,100)
plt.hist(marks,grades,histtype="bar",rwidth=9)
plt.xticks([0,25,50,75,100])
plt.xlabel("Marks")
plt.ylabel("No of students")
plt.show()