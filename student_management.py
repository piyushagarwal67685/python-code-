class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("\nStudent Details")
        print("Student ID :", self.student_id)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Course     :", self.course)
        print("-" * 30)


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self):
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        student = Student(student_id, name, age, course)
        self.students.append(student)

        print("Student Added Successfully!")

    def search_student(self):
        student_id = input("Enter Student ID to Search: ")

        for student in self.students:
            if student.student_id == student_id:
                print("\nStudent Found!")
                student.display()
                return

        print("Student Not Found!")

    def update_student(self):
        student_id = input("Enter Student ID to Update: ")

        for student in self.students:
            if student.student_id == student_id:
                student.name = input("Enter New Name: ")
                student.age = input("Enter New Age: ")
                student.course = input("Enter New Course: ")

                print("Record Updated Successfully!")
                return

        print("Student Not Found!")

    def delete_student(self):
        student_id = input("Enter Student ID to Delete: ")

        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Record Deleted Successfully!")
                return

        print("Student Not Found!")

    def display_all_students(self):
        if len(self.students) == 0:
            print("No Student Records Found!")
        else:
            print("\nAll Student Records")
            for student in self.students:
                student.display()


# Object Creation
sms = StudentManagementSystem()

while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        sms.add_student()

    elif choice == "2":
        sms.search_student()

    elif choice == "3":
        sms.update_student()

    elif choice == "4":
        sms.delete_student()

    elif choice == "5":
        sms.display_all_students()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")