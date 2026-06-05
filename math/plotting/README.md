This contains the code for this module 

plt.xlim(0, 10) #set limit
plt.plot(y, color="red") #change color
plt.show() #show

plt.title("Men's Height vs Weight")
plt.xlabel("Height (in)")
plt.ylabel("Weight (lbs)")
plt.scatter(x, y, color="magenta")
plt.yscale("log")

 # 2 Lines 
plt.plot(x, y1, color="red", linestyle="--", label='C-14')
plt.plot(x, y2, color="green", linestyle="-", label='Ra-226')
plt.legend(loc='upper right')

# x ticks
plt.hist(student_grades, bins=np.arange(0, 110, 10), edgecolor='black')
plt.xticks(np.arange(0, 110, 10))