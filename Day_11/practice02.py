message = input("Enter your message:")

with open("message.txt","a") as file:
    file.write(message + "\n")

print("Message saved successfully.")

