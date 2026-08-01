file = open("student.txt","w")
file.write("Name: Shivam\n")
file.write("Course: Python\n")


file = open("student.txt","a")
file.write("Goal: Become a Python Developer")
file.close()


file = open("student.txt","r")
print(file.read())
file.close()
