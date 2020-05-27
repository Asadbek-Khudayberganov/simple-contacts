contacts = {}
terminate = False

while not terminate:
    command = input('A)dd D)elete L)ook up Q)uit: ')
    if command == 'A' or command == 'a':
        name = input("Enter a new name: ")
        print('Enter phone number for', name, end=':')
        number = input()
        contacts[name] = number
    elif command == 'D' or command == 'd':
        name = input('Enter name to delete: ')
        del contacts[name]
    elif command == 'L' or command == 'l':
        name  = input('Enter a name: ')
        print(name, contacts[name])
    elif command == 'Q' or command == 'q':
        terminate = True
    elif command == 'dump':
        print(contacts)
    else:
        print(command, 'is not a valid command')
