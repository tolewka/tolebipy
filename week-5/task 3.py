class Person:
    def __init__(self, name):
        self.name = name

    def get_info(self):
        return f"Person name: {self.name}"


class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id

    def get_info(self):
        return f"Student name: {self.name}, ID: {self.student_id}"


person = Person("John")
student = Student("Ali", "S123")

print(person.get_info())
print(student.get_info())
