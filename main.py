contacts = []

choice = ''
while choice != '0':
    print("1. Add")
    print("2. List")
    print("3. Search by name")
    print("4. Search by mobile")
    print("0. Exit")
    choice = input("Enter a choice: ")
    if choice == '1':
        name = input("Enter new contact name: ")
        mobile = input("Enter new contact mobile: ")
        contact = [name, mobile]
        contacts.append(contact)
        print("new contact was added")
    elif choice == '2':
        for contact in contacts:
            print(contact)
