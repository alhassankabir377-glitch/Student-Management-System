import sqlite3


class Student:
    """Represents a student."""

    def __init__(self, name, age, course, level):
        self.name = name
        self.age = age
        self.course = course
        self.level = level


class StudentManager:

    def __init__(self):
        self.connection = sqlite3.connect("school.db")
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL,
            level INTEGER NOT NULL
        )
        """)
        self.connection.commit()

    def add_student(self):
        print("\n========== ADD STUDENT ==========")

        while True:
            name = input("Enter student name: ").strip()
            if name:
                name = name.title()
                break
            print("Invalid name. Please enter a valid name.")

        self.cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
        if self.cursor.fetchone():
            print("Student already exists!")
            return

        while True:
            try:
                age = int(input("Enter student age: ").strip())
                if 15 <= age <= 60:
                    break
                print("Age must be between 15 and 60.")
            except ValueError:
                print("Enter a valid number.")

        while True:
            course = input("Enter student course: ").strip()
            if course:
                break
            print("Invalid course. Please enter a valid course.")

        while True:
            try:
                level = int(input("Enter student level: ").strip())
                break
            except ValueError:
                print("Invalid level. Please enter a valid level.")

        student = Student(name, age, course, level)
        self.cursor.execute(
            "INSERT INTO students (name, age, course, level) VALUES (?, ?, ?, ?)",
            (student.name, student.age, student.course, student.level),
        )
        self.connection.commit()
        print("\nStudent added successfully.")

    def view_students(self):
        self.cursor.execute("SELECT * FROM students")
        students = self.cursor.fetchall()

        if not students:
            print("\nNo students found.")
            return

        print("\n========== STUDENT RECORDS ==========")
        for student in students:
            print(f"ID     : {student[0]}")
            print(f"Name   : {student[1]}")
            print(f"Age    : {student[2]}")
            print(f"Course : {student[3]}")
            print(f"Level  : {student[4]}")
            print("--------------------------------------")

    def search_student(self):
        name = input("Enter student name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return

        self.cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
        student = self.cursor.fetchone()

        if student:
            print("\nStudent Found")
            print(f"ID     : {student[0]}")
            print(f"Name   : {student[1]}")
            print(f"Age    : {student[2]}")
            print(f"Course : {student[3]}")
            print(f"Level  : {student[4]}")
        else:
            print("\nStudent not found.")

    def update_student(self):
        while True:
            student_id = input("Enter student ID to update: ").strip()
            if student_id:
                try:
                    student_id = int(student_id)
                    break
                except ValueError:
                    print("Please enter a valid numeric ID.")
            else:
                print("Student ID cannot be empty.")

        self.cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        student = self.cursor.fetchone()

        if not student:
            print("\nStudent not found.")
            return

        print("\nCurrent Student Details:")
        print(f"ID     : {student[0]}")
        print(f"Name   : {student[1]}")
        print(f"Age    : {student[2]}")
        print(f"Course : {student[3]}")
        print(f"Level  : {student[4]}")

        while True:
            try:
                new_level = int(input("Enter new level: ").strip())
                break
            except ValueError:
                print("Please enter a valid integer for level.")

        self.cursor.execute(
            "UPDATE students SET level = ? WHERE id = ?",
            (new_level, student_id),
        )
        self.connection.commit()
        print("Student updated successfully.")

    def close(self):
        self.connection.close()


def display_menu():
    print("\n==============================")
    print("STUDENT MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student Level")
    print("5. Exit")
    print("==============================")


def main():
    manager = StudentManager()

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.search_student()
        elif choice == "4":
            manager.update_student()
        elif choice == "5":
            manager.close()
            print("\nThank you for using the Student Management System.")
            break
        else:
            print("\nInvalid choice.")


if __name__ == "__main__":
    main()
