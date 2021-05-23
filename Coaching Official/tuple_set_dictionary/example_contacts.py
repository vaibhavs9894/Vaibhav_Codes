# program where user can add contacts for contact book/ display them
# user has to enter a contact name
# if the name is not given the program quit
# if the contact is available then the number is shown
# else if the contact is not available the number is asked from user to save

contacts = {'help': 100}
print('Your temp contact book')
while True:
    print('-*-' * 25)
    name = input("=> enter contact name : ")
    if name:
        if name in contacts:
            print('=> contact found')
            print(f'=> {name} : {contacts[name]}')
        else:
            print('=> contact not found')
            update = input('>> do you want to add the contact(Y/N)?')
            if update.lower() == 'y':
                number = input(f'>> enter contact number for {name}')
                contacts[name] = number
                print(f'=> contact updated for {name}')
    else:
        print('closing contact book')
        break