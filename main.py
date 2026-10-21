from db_functions import delete_student, list_students

def show_remaining():
    students = list_students()
    names = [row[1] for row in students]
    print(f"Remaining students ({len(names)}): {', '.join(names)}")

def handle_command(text):
    text = text.lower().strip()

    if text.startswith("delete "):
        name = text.replace("delete ", "", 1).strip()
        if delete_student(name):
            print(f"{name.title()} deleted.")
        else:
            print(f"{name.title()} not found.")
        show_remaining()

    elif text == "list":
        show_remaining()

    else:
        print("Sorry, I only understand 'delete <name>' or 'list'.")

while True:
    command = input("Command (or 'quit'): ")
    if command == "quit":
        break
    handle_command(command)