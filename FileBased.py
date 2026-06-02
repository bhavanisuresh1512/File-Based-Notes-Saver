# File-Based Notes Saver

FILE_NAME = "notes.txt"

def add_note():
    note = input("Enter your note: ")

    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")

    print("Note saved successfully!")

def view_notes():
    try:
        with open(FILE_NAME, "r") as file:
            notes = file.read()

            if notes.strip() == "":
                print("No notes found.")
            else:
                print("\n----- Saved Notes -----")
                print(notes)
                print("-----------------------")

    except FileNotFoundError:
        print("No notes file found. Add a note first.")

def main():
    while True:
        print("\n=== Notes Saver ===")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
