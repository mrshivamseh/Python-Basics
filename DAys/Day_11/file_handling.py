file = open("notes.txt","w")

file.write("Hello python!")

file.close()

print("Data written successfully.")




file = open("notes.txt","r")

data = file.read()

print(data)

file.close()



file = open("notes.txt","a")

file.write("\nThis is a new line.")

file.close()

print("Data appended successfully.")


