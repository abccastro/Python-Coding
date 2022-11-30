"""
Create a program that a user can use to manage the primary email address
and phone number for a contact.
Created by: Auradee Castro
"""

contact_manager_list = []


def displayCommandMenu():
    print("Contact Manager")
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")

    while True:
        command = input("Command: ")

        if command == "list":
            displayContactList()
        elif command == "view":
            viewContact()
        elif command == "add":
            addContact()
        elif command == "del":
            deleteContact()
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Invalid command!")


def displayContactList():
    if len(contact_manager_list) == 0:
        print("Empty contact list")
    else:
        for idx, contact in enumerate(contact_manager_list):
            print(str(idx+1) + ".", contact[0])


def viewContact():
    if len(contact_manager_list) == 0:
        print("Empty contact list")
    else:
        view_number = input("Number: ")

        if not view_number.isdigit() or int(view_number) > len(contact_manager_list):
            print("Invalid contact number")
        else:
            contact_info = contact_manager_list[int(view_number) - 1]

            print("Number:", int(view_number))
            print("Name:", contact_info[0])
            print("Email:", contact_info[1])
            print("Phone:", contact_info[2])


def addContact():
    name = input("Name: ")
    email = input("Email: ")
    phone_num = input("Phone: ")

    contact_manager_list.append([name, email, phone_num])

    print(name, "was added.")


def deleteContact():
    del_number = input("Number: ")

    if not del_number.isdigit() or int(del_number) > len(contact_manager_list):
        print("Invalid contact number")
    else:
        del_contact = contact_manager_list.pop(int(del_number) - 1)
        print(del_contact[0], "was deleted.")


# Added two records in contact manager list
contact_manager_list.append(["Auradee Castro", "a.castro@hotmail.com", "(437) 52614001"])
contact_manager_list.append(["Terrence Castro", "t.castro@hotmail.com", "(437) 52614002"])

displayCommandMenu()
