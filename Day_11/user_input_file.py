name = input("Enter your name:")
with open("user_data.text","w") as file:
    file.write(name)


print("Name saved successfully.")
