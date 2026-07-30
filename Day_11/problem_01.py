name = input("Enter your name:")
phone = input("Enter your phone number:")

with open("contacts.txt","a") as file:
    file.write("name:"+name+"\n")
    file.write("Phone:"+phone+"\n")

    file.write("-----------\n")

print("Contact saved successfully.")

