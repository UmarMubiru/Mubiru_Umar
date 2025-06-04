class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")

class Lecturer(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")

class Staff(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

# Example usage:
print("=== Student ===")
s = Student("Alice", 20, "S001")
s.display_info()

print("\n=== Lecturer ===")
l = Lecturer("Dr. Brian", 45, "Mathematics")
l.display_info()

print("\n=== Staff ===")
st = Staff("Mr. Dan", 38, "Admissions")
st.display_info()




