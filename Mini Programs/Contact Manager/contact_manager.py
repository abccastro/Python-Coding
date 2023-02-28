"""
Create a program that a user can use to manage the primary email address
and phone number for a contact.

Submitted by: Auradee Castro
"""
from enum import Enum

CONTACT_FILENAME = "ContactManager.txt"


class Command(Enum):
    List = "list"
    View = "view"
    Add = "add"
    Delete = "del"
    Exit = "exit"


def startContactManager():
    print("+++++++++++++++++++++++++++++++++++++++++")
    print("+             Contact Manager           +")
    print("+++++++++++++++++++++++++++++++++++++++++")
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("del - Delete a contact")
    print("exit - Exit program")

    command = None
    while command != Command.Exit.value:

        command = input("\nCommand: ").strip().lower()

        if command not in [elem.value for elem in Command]:
            print("Invalid selection. Try again.")
        elif command == Command.Exit.value:
            print("Bye!")
            break
        else:
            contact_list = readFile(CONTACT_FILENAME)
            if contact_list is None:
                print("Exiting application...")
                break

            if command == Command.List.value:
                displayContactList(contact_list)
            elif command == Command.View.value:
                viewContact(contact_list)
            elif command == Command.Add.value:
                addContact(contact_list)
            elif command == Command.Delete.value:
                deleteContact(contact_list)

def displayContactList(contact_list):
    if len(contact_list) == 0:
        print("Empty contact list")
    else:
        for idx, contact in enumerate(contact_list, start=1):
            print(f"{idx}. {contact[0]}")

def viewContact(contact_list):
    if len(contact_list) == 0:
        print("Empty contact list")
    else:
        view_number = input("Number: ")
        if not view_number.isdigit() or int(view_number) > len(contact_list):
            print("Invalid contact number")
        else:
            contact_info = contact_list[int(view_number) - 1]
            print(f"Name: {contact_info[0]}")
            print(f"Email: {contact_info[1]}")
            print(f"Phone: {contact_info[2]}")

def addContact(contact_list):
    name = input("Name: ")
    email = input("Email: ")
    phone_num = input("Phone: ")

    contact_list.append([name, email, phone_num])

    is_added = appendFile(contact_list, CONTACT_FILENAME)
    if is_added:
        print(f"{name} was added.")

def deleteContact(contact_list):
    if len(contact_list) == 0:
        print("Empty contact list")
    else:
        del_number = input("Number: ")

        if not del_number.isdigit() or int(del_number) > len(contact_list):
            print("Invalid contact number")
        else:
            del_contact = contact_list.pop(int(del_number) - 1)

            is_deleted = writeFile(contact_list, CONTACT_FILENAME)
            if is_deleted:
                print(f"{del_contact[0]} was deleted.")

def readFile(filename):
    try:
        contact_list = []
        with open(filename, "r") as file:
            line_list = file.readlines()

        ctr = 0
        while ctr < len(line_list)-1:
            contact_details = [line_list[ctr].replace("\n", ""),
                               line_list[ctr+1].replace("\n", ""),
                               line_list[ctr+2].replace("\n", "")]
            contact_list.append(contact_details)
            ctr += 3

    except EOFError:
        contact_list = []
    except Exception as err:
        print(f"Unexpected error: {err}")
        contact_list = None

    return contact_list

def writeFile(contact_list, filename):
    try:
        with open(filename, "w") as file:
            for contact in contact_list:
                for detail in contact:
                    file.write(detail + "\n")
    except Exception as err:
        print(f"Unexpected error: {err}")
        return False

    return True

def appendFile(contact_list, filename):
    try:
        with open(filename, "a") as file:
            contact = contact_list[len(contact_list)-1]
            for detail in contact:
                file.write(detail + "\n")
    except Exception as err:
        print(f"Unexpected error: {err}")
        return False

    return True

if __name__ == "__main__":
    startContactManager()
