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
        print(
            "Could not load saved students. "
            "Starting with an empty list."
        )
        students = []


def save_students():
    os.makedirs(DATA_FOLDER, exist_ok=True)

    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)

    except OSError:
        print("Could not save students.")


def student_id_exists(student_id):
    for student in students:
        if student["id"] == student_id:
            return True

    return False


def add_student(student_id, name, age, course):
    student_id = student_id.strip()
    name = name.strip()
    course = course.strip()

    if not student_id:
        return False

    if student_id_exists(student_id):
        return False

    if not name:
        return False

    if not isinstance(age, int) or age <= 0:
        return False

    if not course:
        return False

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    save_students()

    return True


def find_student_by_id(student_id):
    student_id = student_id.strip()

    for student in students:
        if student["id"] == student_id:
            return student

    return None


def search_students_by_name(name):
    name = name.strip().lower()

    if not name:
        return []

    found_students = []

    for student in students:
        if name in student["name"].lower():
            found_students.append(student)

    return found_students


def update_student(student_id, field, new_value):
    student = find_student_by_id(student_id)

    if student is None:
        return False

    if field == "name":
        new_value = new_value.strip()

        if not new_value:
            return False

        student["name"] = new_value

    elif field == "age":
        if not isinstance(new_value, int) or new_value <= 0:
            return False

        student["age"] = new_value

    elif field == "course":
        new_value = new_value.strip()

        if not new_value:
            return False

        student["course"] = new_value

    else:
        return False

    save_students()
    return True


def delete_student(student_id):
    student = find_student_by_id(student_id)

    if student is None:
        return False

    students.remove(student)
    save_students()

    return True


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


def add_student_menu():
    student_id = input("Enter student ID: ").strip()
    name = input("Enter student name: ").strip()

    try:
        age = int(input("Enter student age: ").strip())

    except ValueError:
        print("Please enter a valid age.")
        return

    course = input("Enter student course: ").strip()

    if add_student(student_id, name, age, course):
        print("\nStudent added successfully!")
    else:
        print(
            "\nCould not add student. "
            "Check for empty fields, invalid age, or duplicate ID."
        )


def search_student_menu():
    if not students:
        print("\nNo students found.")
        return

    print("\n1. Search by ID")
    print("2. Search by Name")

    choice = input("Choose search option: ").strip()

    if choice == "1":
        student_id = input("Enter student ID: ").strip()

        student = find_student_by_id(student_id)

        if student:
            display_student(student)
        else:
            print("Student not found.")

    elif choice == "2":
        name = input("Enter student name: ").strip()

        found_students = search_students_by_name(name)

        if found_students:
            for student in found_students:
                display_student(student)
        else:
            print("Student not found.")

    else:
        print("Invalid search option.")


def update_student_menu():
    if not students:
        print("\nNo students found.")
        return

    student_id = input(
        "\nEnter the Student ID to update: "
    ).strip()

    student = find_student_by_id(student_id)

    if student is None:
        print("Student not found.")
        return

    print("\nCurrent Student Information:")
    display_student(student)

    print("\n1. Update Name")
    print("2. Update Age")
    print("3. Update Course")

    choice = input("Choose what to update: ").strip()

    if choice == "1":
        new_value = input("Enter new name: ")

        success = update_student(
            student_id,
            "name",
            new_value
        )

    elif choice == "2":
        try:
            new_value = int(
                input("Enter new age: ").strip()
            )

        except ValueError:
            print("Please enter a valid age.")
            return

        success = update_student(
            student_id,
            "age",
            new_value
        )

    elif choice == "3":
        new_value = input("Enter new course: ")

        success = update_student(
            student_id,
            "course",
            new_value
        )

    else:
        print("Invalid update option.")
        return

    if success:
        print("Student updated successfully!")
    else:
        print("Invalid update value.")


def delete_student_menu():
    if not students:
        print("\nNo students found.")
        return

    student_id = input(
        "\nEnter the Student ID to delete: "
    ).strip()

    if delete_student(student_id):
        print("Student deleted successfully!")
    else:
        print("Student not found.")


def main():
    load_students()

    while True:
        show_menu()

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            add_student_menu()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student_menu()

        elif choice == "4":
            update_student_menu()

        elif choice == "5":
            delete_student_menu()

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