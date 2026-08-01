with open("profile.txt", "w") as file:
    print(file.write("Hello, World!"))



with open("profile.txt", "r") as file:
    print(file.read())
    