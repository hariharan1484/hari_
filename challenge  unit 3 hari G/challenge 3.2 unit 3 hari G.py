class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __repr__(self):
        return f"Student(name={self.name}, roll_number={self.roll_number}, cgpa={self.cgpa})"

def sort_students(student_list):
    """
    Sorts a list of student objects based on their CGPA in descending order.

    Parameters:
    student_list (list): List of student objects.

    Returns:
    list: Sorted list of student objects based on CGPA in descending order.
    """
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Example usage
students = [
    Student("Alice", "A123", 3.8),
    Student("Bob", "B456", 3.5),
    Student("Charlie", "C789", 3.7),
    Student("David", "D321", 3.9)
]

print("Original student list:")
for student in students:
    print(student)

sorted_students = sort_students(students)

print("\nSorted student list based on CGPA (descending order):")
for student in sorted_students:
    print(student)
