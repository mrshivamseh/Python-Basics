try:
    filename = input("Enter file name:")

    if filename == "":
        raise ValueError("Filename cannot be empty.")

    with open(filename,"r") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found.")

except ValueError as error:
    print(error)

finally:
    print("Program ended.")
    
