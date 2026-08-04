name = input("Enter your name:")
age = input("Enter your age:")
city = input("Enter your city:")

with open("profile.txt","w") as file:
    file.write("Name:" + name + "\n")
    file.write("Age:" + age + "\n")
    file.write("City:" + city)

    print("Profile saved successfully.")
    