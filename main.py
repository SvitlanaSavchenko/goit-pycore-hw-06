from input_parsing import parse_input
from address_book import AddressBook
from contact import Contact

def main():
    address_book = AddressBook()
    print("Welcome to the assistant bot!")
    print("You can use some of these commands:\n add [name] [phone number] \n change [name] [new phone number] \n phone [name] \n all \n close or exit. \n Let's go!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) != 2:
                print("Invalid command.")
            else:
                name, phone = args
                try:
                    contact = Contact(name, phone)
                    address_book.add_record(contact)
                    print("Contact added.")
                except ValueError as e:
                    print(e)
        elif command == "change":
            name, new_phone = args
            record = address_book.search_record_by_name(name)
            if record:
                record.edit_phone(record.phones[0], new_phone)
                print("Contact updated.")
            else:
                print("Contact not found.")
        elif command == "phone":
            name = args[0]
            record = address_book.search_record_by_name(name)
            if record:
                print(record.phones[0])
            else:
                print("Contact not found.")
        elif command == "all":
            if not address_book:
                print("No contacts available.")
            else:
                for record in address_book.values():
                    print(record)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
