print("                    Welcome to the Contact Book Application                    ")

contact_book = {}


def add_contact():
    name = input("Enter contact name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contact_book[name] = {
        "phone_number": phone_number,
        "email": email,
        "address": address
    }
    print(f"Contact '{name}' added successfully!")


def view_contacts():
    if not contact_book:
        print("Contact book is empty.")
    else:
        print("Contacts:")
        for name, contact_info in contact_book.items():
            print(f"Name: {name}")
            print(f"Phone Number: {contact_info['phone_number']}")
            print(f"Email: {contact_info['email']}")
            print(f"Address: {contact_info['address']}")
            print('-' * 20)


def search_contact():
    search_term = input("Enter contact name or phone number to search: ")
    found = False
    for name, contact_info in contact_book.items():
        if search_term in (name, contact_info['phone_number']):
            print(f"Name: {name}")
            print(f"Phone Number: {contact_info['phone_number']}")
            print(f"Email: {contact_info['email']}")
            print(f"Address: {contact_info['address']}")
            found = True
    if not found:
        print("Contact not found.")


def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contact_book:
        print(f"Updating contact '{name}':")
        phone_number = input("Enter new phone number: ")
        email = input("Enter new email: ")
        address = input("Enter new address: ")
        contact_book[name] = {
            "phone_number": phone_number,
            "email": email,
            "address": address
        }
        print(f"Contact '{name}' updated successfully!")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contact_book:
        del contact_book[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print("Contact not found.")


while True:

    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Thankyou for using this Application!")
        break
    else:
        print("Invalid choice. Please try again.")
