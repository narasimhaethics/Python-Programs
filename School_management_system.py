class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def display_info(self):
        print(f"Student ID: {self.student_id}, Name: {self.name}, Grade: {self.grade}")


class Teacher:
    def __init__(self, teacher_id, name, subject):
        self.teacher_id = teacher_id
        self.name = name
        self.subject = subject

    def display_info(self):
        print(f"Teacher ID: {self.teacher_id}, Name: {self.name}, Subject: {self.subject}")


class Course:
    def __init__(self, course_code, course_name, teacher, students):
        self.course_code = course_code
        self.course_name = course_name
        self.teacher = teacher
        self.students = students

    def display_info(self):
        print(f"Course Code: {self.course_code}, Course Name: {self.course_name}")
        print("Teacher:")
        self.teacher.display_info()
        print("Students:")
        for student in self.students:
            student.display_info()


def main():
    students = []
    teachers = []
    courses = []

    # Input students
    num_students = int(input("Enter the number of students: "))
    for i in range(num_students):
        student_id = input(f"Enter student {i + 1} ID: ")
        name = input(f"Enter student {i + 1} name: ")
        grade = input(f"Enter student {i + 1} grade: ")
        students.append(Student(student_id, name, grade))

    # Input teachers
    num_teachers = int(input("Enter the number of teachers: "))
    for i in range(num_teachers):
        teacher_id = input(f"Enter teacher {i + 1} ID: ")
        name = input(f"Enter teacher {i + 1} name: ")
        subject = input(f"Enter teacher {i + 1} subject: ")
        teachers.append(Teacher(teacher_id, name, subject))

    # Input courses
    num_courses = int(input("Enter the number of courses: "))
    for i in range(num_courses):
        course_code = input(f"Enter course {i + 1} code: ")
        course_name = input(f"Enter course {i + 1} name: ")
        teacher_index = int(input("Enter the index of the teacher for this course: "))
        teacher = teachers[teacher_index]
        student_indices = input("Enter the indices of students for this course (comma-separated): ").split(",")
        students_for_course = [students[int(index)] for index in student_indices]
        courses.append(Course(course_code, course_name, teacher, students_for_course))

    # Display information
    print("\nSchool Information:")
    for course in courses:
        course.display_info()
        print("-" * 30)


if __name__ == "__main__":
    main()
