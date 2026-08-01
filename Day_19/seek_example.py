with open('profile.txt', 'r') as file:
    print(file.read())


    file.seek(0)

    print(file.read(20))
