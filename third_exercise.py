contacts = {}

def hello_command(args):
    print("How can I help you?")

def add_contact(args):
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        print("Contact added.")
    else:
        print("Invalid command format. Use: add [name] [phone]")

def change_contact(args):
    if len(args) == 2:
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            print("Contact updated.")
        else:
            print("Contact not found.")
    else:
        print("Invalid command format. Use: change [name] [new_phone]")

def show_phone(args):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            print(contacts[name])
        else:
            print("Contact not found.")
    else:
        print("Invalid command format. Use: phone [name]")

def show_all(args):
    if not contacts:
        print("No contacts found.")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

def exit_command(args):
    print("Good bye!")
    exit()

commands = {
    "hello": hello_command,
    "add": add_contact,
    "change": change_contact,
    "phone": show_phone,
    "all": show_all,
    "close": exit_command,
    "exit": exit_command
}

def process_command(user_input):
    command_parts = user_input.split()
    if not command_parts:
        return

    command = command_parts[0]
    args = command_parts[1:]

    if command in commands:
        commands[command](args)
    else:
        print("Unknown command. Type 'help' for a list of commands.")

def run():
    print("Contact Management Bot is running. Type 'exit' or 'close' to quit.")
    while True:
        user_input = input("Enter a command: ").lower()
        process_command(user_input)

if __name__ == "__main__":
    run()

if __name__ == "__main__":
    console_bot = ConsoleBot()
    console_bot.run()