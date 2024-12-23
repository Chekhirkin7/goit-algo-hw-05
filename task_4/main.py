from functools import wraps

def input_error(func):
	@wraps(func)
	def inner(*args, **kwargs):
		try:
			return(func(*args, *kwargs))
		except ValueError:
			return "Error: Give me name and phone please."
		except KeyError:
			return "Error: Contact not found."
		except IndexError:
			return "Error: Insufficient arguments provided."
	return inner

@input_error
def parse_input(user_input):
	cmd, *args = user_input.split()
	cmd = cmd.strip().lower()
	return cmd, *args

@input_error
def add_contact(args, contacts):
	name, phone = args
	contacts[name] = phone
	return "Contacts added"

@input_error
def change_contact (args, contacts):
	name, new_phone = args
	if name in contacts:
		contacts[name] = new_phone
		return "Contact updated"
	else:
		return f"Error: Contact with name '{name}' not found."

@input_error
def show_phone (args, contacts):
	name = args [0]
	if name in contacts:
		return contacts[name]
	else:
		return f"Error: Contact with name '{name}' not found."

@input_error
def show_all (contacts):
	if not contacts:
		return "Contacts not found"
	
	result = []
	for name, phone in contacts.items():
		result.append(f"{name}: {phone}")
	
	return "\n".join(result)

def main ():
	contacts = {}
	print("Welcome to the assistant bot")
	while True:
		user_input = input("Enter a command: ")
		command, *args = parse_input(user_input)

		if command in ["close", "exit"]:
			print("Good bye!")
			break

		elif command == "hello":
			print("How can I help you?")
		
		elif command == "add":
			print(add_contact(args, contacts))

		elif command == "change":
			print(change_contact(args, contacts))
		
		elif command == "phone":
			print(show_phone(args, contacts))

		elif command == "all":
			print(show_all(contacts))

		else:
			print("Invalid command")

if __name__ == "__main__":
	main()