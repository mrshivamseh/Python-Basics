try:
    filename = input("Enter file name:")

    with open(filename,"r") as file:
        data = file.read()

    print(data)

except FileNotFoundError:
    print("File not found.")

finally:
    print("Program completed.")

