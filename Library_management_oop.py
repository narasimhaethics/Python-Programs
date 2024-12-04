class Student:
    def __init__(self):
        self.__Studentid = ""
        self.__Studentname = ""
        self.__Studentdept = ""
        self.__Studentemailid = ""
        self.__Studentpassword = ""

    def setStudentid(self, stuid):
        self.__Studentid = stuid

    def getStudentid(self):
        return self.__Studentid

    def setStudentname(self, name):
        self.__Studentname = name

    def getStudentname(self):
        return self.__Studentname

    def setStudentdept(self, dept):
        self.__Studentdept = dept

    def getStudentdept(self):
        return self.__Studentdept

    def setStudentemailid(self, email):
        self.__Studentemailid = email

    def getStudentemailid(self):
        return self.__Studentemailid

    def setStudentpassword(self, password):
        self.__Studentpassword = password

    def getStudentpassword(self):
        return self.__Studentpassword


class Staff:
    def __init__(self):
        self.__Staffid = ""
        self.__Staffname = ""
        self.__Staffdept = ""

    def setStaffid(self, stid):
        self.__Staffid = stid

    def getStaffid(self):
        return self.__Staffid

    def setStaffname(self, name):
        self.__Staffname = name

    def getStaffname(self):
        return self.__Staffname

    def setStaffdept(self, dept):
        self.__Staffdept = dept

    def getStaffdept(self):
        return self.__Staffdept


class Librarian:
    def __init__(self, librarian_id, librarian_name):
        self.__librarian_id = librarian_id
        self.__librarian_name = librarian_name

    def getLibrarianId(self):
        return self.__librarian_id

    def getLibrarianName(self):
        return self.__librarian_name


class Login:
    def __init__(self):
        self.credentials = {"librarian": {"id": "admin", "password": "admin123"}}

    def validate_user(self, role, user_id, password):
        if role in self.credentials and self.credentials[role]["id"] == user_id and self.credentials[role]["password"] == password:
            print(f"{role.capitalize()} login successful!")
            return True
        print("Invalid credentials!")
        return False


class Library:
    def __init__(self):
        self.books = {}  # book_id -> {"title": str, "author": str, "copies": int}
        self.issued_books = {}  # student_id -> [book_id]
        self.students = {}  # student_id -> Student object
        self.staff_members = {}  # staff_id -> Staff object

    # Student Management
    def add_student(self):
        student = Student()
        student.setStudentid(input("Enter Student ID: "))
        student.setStudentname(input("Enter Student Name: "))
        student.setStudentdept(input("Enter Student Department: "))
        student.setStudentemailid(input("Enter Student Email: "))
        student.setStudentpassword(input("Enter Student Password: "))
        if student.getStudentid() in self.students:
            print("Student already exists!")
        else:
            self.students[student.getStudentid()] = student
            print(f"Student {student.getStudentname()} added successfully!")

    def view_students(self):
        print("List of Students:")
        for student_id, student in self.students.items():
            print(f"ID: {student_id}, Name: {student.getStudentname()}, Dept: {student.getStudentdept()}")

    # Staff Management
    def add_staff(self):
        staff = Staff()
        staff.setStaffid(input("Enter Staff ID: "))
        staff.setStaffname(input("Enter Staff Name: "))
        staff.setStaffdept(input("Enter Staff Department: "))
        if staff.getStaffid() in self.staff_members:
            print("Staff already exists!")
        else:
            self.staff_members[staff.getStaffid()] = staff
            print(f"Staff {staff.getStaffname()} added successfully!")

    def view_staff(self):
        print("List of Staff:")
        for staff_id, staff in self.staff_members.items():
            print(f"ID: {staff_id}, Name: {staff.getStaffname()}, Dept: {staff.getStaffdept()}")

    # Book Management
    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Book Author: ")
        copies = int(input("Enter Number of Copies: "))
        if book_id in self.books:
            self.books[book_id]["copies"] += copies
        else:
            self.books[book_id] = {"title": title, "author": author, "copies": copies}
        print(f"Book '{title}' added successfully!")

    def view_books(self):
        print("Available Books:")
        for book_id, details in self.books.items():
            print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Copies: {details['copies']}")

    # Issue and Return Books
    def issue_book(self):
        student_id = input("Enter Student ID: ")
        book_id = input("Enter Book ID: ")
        if student_id not in self.students:
            print("Invalid student ID!")
            return

        if book_id not in self.books or self.books[book_id]["copies"] == 0:
            print("Book not available!")
            return

        if student_id not in self.issued_books:
            self.issued_books[student_id] = []

        self.issued_books[student_id].append(book_id)
        self.books[book_id]["copies"] -= 1
        print(f"Book '{self.books[book_id]['title']}' issued to Student {student_id}!")

    def return_book(self):
        student_id = input("Enter Student ID: ")
        book_id = input("Enter Book ID: ")
        if student_id not in self.issued_books or book_id not in self.issued_books[student_id]:
            print("No record of this book being issued to the student!")
            return

        self.issued_books[student_id].remove(book_id)
        self.books[book_id]["copies"] += 1
        print(f"Book '{self.books[book_id]['title']}' returned by Student {student_id}!")

    # View Issued Books
    def view_issued_books(self):
        print("Issued Books:")
        for student_id, book_list in self.issued_books.items():
            student_name = self.students[student_id].getStudentname()
            print(f"Student: {student_name} (ID: {student_id})")
            for book_id in book_list:
                print(f"  - {self.books[book_id]['title']} by {self.books[book_id]['author']}")

    # Generate Report
    def generate_report(self):
        print("\nLibrary Report:")
        print("\nStudents:")
        self.view_students()
        print("\nStaff:")
        self.view_staff()
        print("\nBooks:")
        self.view_books()
        print("\nIssued Books:")
        self.view_issued_books()


# Main Menu
if __name__ == "__main__":
    login = Login()
    if not login.validate_user("librarian", input("Enter User ID: "), input("Enter Password: ")):
        exit()
    
