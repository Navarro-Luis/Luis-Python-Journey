#You need to create a simple School Management System that models 
# students, teachers, and courses.

class Student:
    def __init__(self, name, student_ID):
        self.name = name
        self.student_ID = student_ID
        self.courses = []
    def enroll(self, course):
        self.courses.append(course)
        print(f'The student is now enrolled in {course.name}')
    def __str__(self):
        courses_str = ', '.join(course.name for course in self.courses)
        return f'Student: {self.name} (ID: {self.student_ID}), Courses: [{courses_str}]'

class Teacher: 
    def __init__(self, name, teacher_ID):
        self.name = name
        self.teacher_ID = teacher_ID
        self.courses = []
    def assign_course(self,course):
        self.courses.append(course)
        print(f'{self.name} is now assigned to {course.name}')
    def __str__(self):
        courses_str = ', '.join(course.name for course in self.courses)
        return f'Teacher: {self.name} (ID: {self.teacher_ID}), Courses: [{courses_str}]'

            
class Class:
    def __init__(self, name, course_ID):
        self.name = name
        self.course_ID = course_ID
        self.students = []
        self.course_teacher = []
    def add_student(self,student):
        self.students.append(student)
        print(f"{student.name} is now added to the course")
    def assign_teacher(self, teacher):
        self.course_teacher.append(teacher)
        print(f"{teacher.name} is the teacher of the course")
    def __str__(self):
        students_str = ', '.join(student.name for student in self.students)
        teacher_name = self.teacher.name if self.teacher else 'None'
        return f"Course: {self.name} (ID: {self.course_ID}), Teacher: {teacher_name}, Students: [{students_str}]"




#in action

student1 = Student("Luis", "191919")
student2 = Student("seif","299492")

teacher1 = Teacher("bob","32124")
teacher2 = Teacher("marley","29299")

course1 = Class("math", "1010101")
course2 = Class("spanish","39319")

course1.add_student(student1)
course1.add_student(student2)

course1.assign_teacher(teacher1)
course2.assign_teacher(teacher2)

student1.enroll(course1)
student2.enroll(course1)

teacher1.assign_course(course1)
teacher2.assign_course(course2)

print(student1)