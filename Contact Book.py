# Contact Book

contacts = {}


def add_contact():
    try:
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")

        contacts[name] = [phone, email]

        print("Contact added successfully!")

    except:
        print("Something went wrong!")


def search_contact():
    try:
        name = input("Enter Name: ")

        if name in contacts:
            print("Name:", name)
            print("Phone:", contacts[name][0])
            print("Email:", contacts[name][1])
        else:
            print("Contact not found!")

    except:
        print("Something went wrong!")


def view_contacts():
    try:
        if len(contacts) == 0:
            print("No contacts found!")

        else:
            for name in contacts:
                print("Name:", name)
                print("Phone:", contacts[name][0])
                print("Email:", contacts[name][1])
                print("----------------")

    except:
        print("Something went wrong!")


while True:

    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. View Contacts")
    print("4. Exit")

    try:
        choice = input("Enter choice: ")

        if choice == "1":
            add_contact()

        elif choice == "2":
            search_contact()

        elif choice == "3":
            view_contacts()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")

    except:
        print("Please enter a valid choice!")
