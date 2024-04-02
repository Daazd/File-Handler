import os

while True:
    menu = int(input('What operation would you like to perform?\n1. Create a file\n2. Add data to a file\n3. Read data from a file\n4. Overwrite a file\n5. Delete a file\n6. Exit\n'))
    if menu == 6:
        break

    name = input('Enter the name of the file: \n')

    if menu in [1, 2, 4]:
        data = input('Enter the data you would like to add to the file: \n')

    try:
        if menu == 1:
            with open(f'{name}.txt', 'w') as f:
                f.write(data)
        elif menu == 2:
            with open(f'{name}.txt', 'a') as f:
                f.write(data)
        elif menu == 3:
            with open(f'{name}.txt', 'r') as f:
                print(f.read())
        elif menu == 4:
            with open(f'{name}.txt', 'w') as f:
                f.write(data)
        elif menu == 5:
            os.remove(f'{name}.txt')
        else:
            print("Invalid option. Please try again.")
    except FileNotFoundError:
        print("File not found. Please try again.")
