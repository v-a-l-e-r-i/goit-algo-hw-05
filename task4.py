def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "There is no such contact!"

    return inner


@input_error
def change_phone(args: list, contacts: dict) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact updated!"


@input_error
def show_phone(name: str, contacts: dict) -> str:
    return f"{name.title()}: {contacts[name]}"


@input_error
def add_contact(args: list, contacts: dict) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact added!"


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter a command: ").strip().casefold()
        match command.split(" "):
            case ['hello']:
                print("How can I help you?")
            case ['all']:
                for key, value in contacts.items():
                    print(f"{key.title()}: {value}")
            case "add", *info:
                print(add_contact(info, contacts))
            case "change", *info:
                print(change_phone(info, contacts))
            case "phone", name:
                print(show_phone(name, contacts))
            case ["close"] | ["exit"]:
                print("Good bye!")
                break
            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()
