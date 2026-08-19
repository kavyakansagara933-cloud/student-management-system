import json
import os


DATA_FOLDER = "data"
DATA_FILE = os.path.join(DATA_FOLDER, "students.json")

students = []


def load_students():
    global students

    if not os.path.exists(DATA_FILE):
        students = []
        return

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            students = json.load(file)

    except (json.JSONDecodeError, OSError):
        print("Could not load saved students. Starting with an empty list.")
        students = []


def save_students():
    os.makedirs(DATA_FOLDER, exist_ok=True)

    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)

    except OSError:
        print("Could not save students.")


def show_menu():
    print("\n" + "=" * 35)
    print("   STUDENT MANAGEMENT SYSTEM")
    print("=" * 35)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


def student_id_exists(student_id):
    for student in students:
        if student["id"] == student_id:
            return True

    return False


def add_student():
    student_id = input("Enter student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if student_id_exists(student_id):
        print("A student with this ID already exists.")
        return

    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    try:
        age = int(input("Enter student age: ").strip())

        if age <= 0:
            print("Age must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid age.")
        return

    course = input("Enter student course: ").strip()

    if not course:
        print("Course cannot be empty.")
        return

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    save_students()

    print("\nStudent added successfully!")


def view_students():
    if not students:
        print("\nNo students found.")
        return

    print("\n" + "=" * 35)
    print("        STUDENT LIST")
    print("=" * 35)

    for number, student in enumerate(students, start=1):
        print(f"\nStudent {number}")
        print(f"ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Course: {student['course']}")


def display_student(student):
    print("\nStudent Found:")
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Course: {student['course']}")


def search_student():
    if not students:
        print("\nNo students found.")
        return

    print("\n1. Search by ID")
    print("2. Search by Name")

    choice = input("Choose search option: ").strip()

    if choice == "1":
        student_id = input("Enter student ID: ").strip()

        for student in students:
            if student["id"] == student_id:
                display_student(student)
                return

        print("Student not found.")

    elif choice == "2":
        name = input("Enter student name: ").strip().lower()

        found_students = []

        for student in students:
            if name in student["name"].lower():
                found_students.append(student)

        if found_students:
            for student in found_students:
                display_student(student)
        else:
            print("Student not found.")

    else:
        print("Invalid search option.")


def update_student():
    if not students:
        print("\nNo students found.")
        return

    student_id = input(
        "\nEnter the Student ID to update: "
    ).strip()

    student_to_update = None

    for student in students:
        if student["id"] == student_id:
            student_to_update = student
            break

    if student_to_update is None:
        print("Student not found.")
        return

    print("\nCurrent Student Information:")
    display_student(student_to_update)

    print("\n1. Update Name")
    print("2. Update Age")
    print("3. Update Course")

    choice = input("Choose what to update: ").strip()

    if choice == "1":
        new_name = input("Enter new name: ").strip()

        if new_name:
            student_to_update["name"] = new_name
            save_students()
            print("Student name updated successfully!")
        else:
            print("Name cannot be empty.")

    elif choice == "2":
        try:
            new_age = int(
                input("Enter new age: ").strip()
            )

            if new_age > 0:
                student_to_update["age"] = new_age
                save_students()
                print("Student age updated successfully!")
            else:
                print("Age must be greater than 0.")

        except ValueError:
            print("Please enter a valid age.")

    elif choice == "3":
        new_course = input("Enter new course: ").strip()

        if new_course:
            student_to_update["course"] = new_course
            save_students()
            print("Student course updated successfully!")
        else:
            print("Course cannot be empty.")

    else:
        print("Invalid update option.")


def delete_student():
    if not students:
        print("\nNo students found.")
        return

    student_id = input(
        "\nEnter the Student ID to delete: "
    ).strip()

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students()

            print(
                f"Student '{student['name']}' "
                "deleted successfully!"
            )
            return

    print("Student not found.")


def main():
    load_students()

    while True:
        show_menu()

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("\nGoodbye!")
            break

        else:
            print(
                "\nInvalid option. "
                "Please choose 1, 2, 3, 4, 5, or 6."
            )


if __name__ == "__main__":
    main()