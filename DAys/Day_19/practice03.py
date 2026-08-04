with open('profile.txt', 'w') as file:
    file.write("Name: Shivam\n")
    file.write("Goal: Python Developer\n")
    file.write("City: Delhi\n")

with open('profile.txt', 'r') as file:
    print(file.read())

