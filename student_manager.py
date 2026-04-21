import json
import os

FILE_NAME = "students.json"

# ------------------ Utility Functions ------------------

def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}
    return {}

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# ------------------ Core Features ------------------

def add_student(data):
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty!")
        return

    if name in data:
        print("Student already exists!")
        return

    try:
        marks = int(input("Enter marks (0-100): "))
        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100!")
            return

        data[name] = marks
        save_data(data)
        print(f"{name} added successfully!")

    except ValueError:
        print("Invalid input! Enter numeric marks.")

def view_students(data):
    if not data:
        print("No students found!")
        return

    print("\n--- Student List ---")
    for name, marks in data.items():
        print(f"{name} : {marks}")

def check_result(data):
    name = input("Enter student name: ").strip()

    if name in data:
        marks = data[name]
        result = "PASS" if marks >= 40 else "FAIL"
        print(f"{name} → {marks} → {result}")
    else:
        print("Student not found!")

def update_student(data):
    name = input("Enter student name to update: ").strip()

    if name in data:
        try:
            marks = int(input("Enter new marks (0-100): "))
            if marks < 0 or marks > 100:
                print("Marks must be between 0 and 100!")
                return

            data[name] = marks
            save_data(data)
            print("Updated successfully!")

        except ValueError:
            print("Invalid marks!")
    else:
        print("Student not found!")

def delete_student(data):
    name = input("Enter student name to delete: ").strip()

    if name in data:
        del data[name]
        save_data(data)
        print("Deleted successfully!")
    else:
        print("Student not found!")

# ------------------ Main Program ------------------

def main():
    data = load_data()

    while True:
        print("\n===== STUDENT MANAGER APP =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Check Result")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(data)
        elif choice == "2":
            view_students(data)
        elif choice == "3":
            check_result(data)
        elif choice == "4":
            update_student(data)
        elif choice == "5":
            delete_student(data)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
