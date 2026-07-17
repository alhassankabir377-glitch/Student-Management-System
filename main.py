
import csv
from typing import Optional, List

class Student:
    """Represents a student with name, age, course, and level."""
    
    def __init__(self, name: str, age: int, course: str, level: int):
        """
        Initialize a Student object.
        
        Args:
            name: Student's full name
            age: Student's age
            course: Course name
            level: Academic level
        """
        self.name = name
        self.age = age
        self.course = course
        self.level = level
    
    def to_dict(self) -> dict:
        """Convert student object to dictionary for JSON serialization."""
        return {
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "level": self.level
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Student':
        """Create a Student object from a dictionary."""
        return cls(data["name"], data["age"], data["course"], data["level"])
    
    def __str__(self) -> str:
        """String representation of student."""
        return (f"Name   : {self.name}\n"
                f"Age    : {self.age}\n"
                f"Course : {self.course}\n"
                f"Level  : {self.level}")


class StudentRecordSystem:
    """Manages a collection of student records with persistence to CSV."""
    
    def __init__(self, filename: str = "students.csv"):
        """
        Initialize the StudentRecordSystem.
        
        Args:
            filename: Path to CSV file for storing student records
        """
        self.filename = filename
        self.students: List[Student] = []
        self.load_students()
    
    def load_students(self) -> None:
        """Load students from CSV file."""
        try:
            with open(self.filename, "r", newline="") as file:
                reader = csv.DictReader(file)
                self.students = []
                for row in reader:
                    if row and row.get("Name"):  # Skip empty rows
                        try:
                            student = Student(
                                name=row["Name"],
                                age=int(row["Age"]),
                                course=row["Course"],
                                level=int(row["Level"])
                            )
                            self.students.append(student)
                        except (ValueError, KeyError):
                            continue
        except FileNotFoundError:
            self.students = []
    
    def save_students(self) -> None:
        """Save students to CSV file."""
        with open(self.filename, "w", newline="") as file:
            fieldnames = ["Name", "Age", "Course", "Level"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in self.students:
                writer.writerow({
                    "Name": student.name,
                    "Age": student.age,
                    "Course": student.course,
                    "Level": student.level
                })
    
    def student_exists(self, name: str) -> bool:
        """Check if a student exists by name."""
        return any(student.name.lower() == name.lower() for student in self.students)
    
    def find_student(self, name: str) -> Optional[Student]:
        """Find a student by name."""
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None
    
    def add_student(self) -> None:
        """Prompt user to add a new student."""
        # Get student name
        while True:
            name = input("Enter student name: ").strip()
            if name:
                break
            print("Name cannot be empty! Please try again.")
        
        name = name.title()
        
        # Check if student already exists
        if self.student_exists(name):
            print("Student already exists!")
            return
        
        # Get student age
        while True:
            try:
                age = int(input("Enter student age: "))
                break
            except ValueError:
                print("Please enter a valid age.")
        
        # Get student course
        course = input("Enter student course: ").strip()
        
        # Get student level
        while True:
            try:
                level = int(input("Enter student level: "))
                break
            except ValueError:
                print("Please enter a valid level.")
        
        # Create and add student
        student = Student(name, age, course, level)
        self.students.append(student)
        self.save_students()
        print("Student added successfully!")
    
    def view_students(self) -> None:
        """Display all student records."""
        if not self.students:
            print("\nNo students found.\n")
            return
        
        print("\n========== STUDENT RECORDS ==========")
        
        for i, student in enumerate(self.students, start=1):
            print(f"\nStudent {i}")
            print("-------------------------")
            print(student)
        
        print("\n=====================================")
        print(f"Total Students: {len(self.students)}\n")
    
    def search_student(self) -> None:
        """Search for a student by name."""
        while True:
            name = input("Enter student name to search: ").strip()
            if name:
                break
            print("Name cannot be empty! Please try again.")
        
        student = self.find_student(name)
        
        if student:
            print("\nStudent Found!")
            print("-------------------------")
            print(student)
        else:
            print("Student not found.")
    
    def update_student(self) -> None:
        """Prompt user to update a student's details."""
        while True:
            name = input("Enter student name to update: ").strip()
            if name:
                break
            print("Name cannot be empty! Please try again.")
        
        student = self.find_student(name)
        
        if not student:
            print("Student not found.")
            return
        
        print("\nLeave blank to keep the current value.\n")
        
        # Update name
        new_name = input(f"Name ({student.name}): ").strip()
        if new_name:
            student.name = new_name.title()
        
        # Update age
        new_age = input(f"Age ({student.age}): ").strip()
        if new_age:
            try:
                student.age = int(new_age)
            except ValueError:
                print("Invalid age, keeping current value.")
        
        # Update course
        new_course = input(f"Course ({student.course}): ").strip()
        if new_course:
            student.course = new_course
        
        # Update level
        new_level = input(f"Level ({student.level}): ").strip()
        if new_level:
            try:
                student.level = int(new_level)
            except ValueError:
                print("Invalid level, keeping current value.")
        
        self.save_students()
        print("Student updated successfully!")
    
    def delete_student(self) -> None:
        """Prompt user to delete a student."""
        while True:
            name = input("Enter student name to delete: ").strip()
            if name:
                break
            print("Name cannot be empty! Please try again.")
        
        student = self.find_student(name)
        
        if not student:
            print("Student not found.")
            return
        
        print(f"\nAre you sure you want to delete {student.name}? (yes/no): ", end="")
        confirm = input().strip().lower()
        
        if confirm in ("yes", "y"):
            self.students.remove(student)
            self.save_students()
            print("Student deleted successfully!")
        else:
            print("Delete operation cancelled.")
    
    def get_total_students(self) -> int:
        """Return the total number of students."""
        return len(self.students)


def main():
    """Main program loop."""
    system = StudentRecordSystem("students.csv")
    
    while True:
        print("\n=====================================")
        print("STUDENT RECORD MANAGEMENT SYSTEM")
        print(f"Total Students: {system.get_total_students()}")
        print("=====================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("=====================================")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            system.add_student()
        elif choice == "2":
            system.view_students()
        elif choice == "3":
            system.search_student()
        elif choice == "4":
            system.update_student()
        elif choice == "5":
            system.delete_student()
        elif choice == "6":
            print("Thank you for using the Student Record Management System.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()