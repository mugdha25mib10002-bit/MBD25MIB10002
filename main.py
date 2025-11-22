from database import init_db
from auth import login
from student import StudentService
from course import CourseService
from enrollment import EnrollmentService
from grade import GradeService

def menu():
    print("""
=== STUDENT MANAGEMENT SYSTEM ===
1. Register student
2. Add course
3. Enroll student
4. Add grade
5. List students
6. List courses
7. List enrollments for student
8. List grades for student
0. Exit
""")

def main():
    init_db()
    user = login()
    if not user:
        return

    student_svc = StudentService()
    course_svc = CourseService()
    enroll_svc = EnrollmentService()
    grade_svc = GradeService()

    while True:
        menu()
        ch = input("Choose: ").strip()
        if ch == "0":
            break
        elif ch == "1":
            s = student_svc.create(input("Name: "), input("DOB (YYYY-MM-DD): "), input("Email: "), input("Phone: "))
            print("Student created:", s)
        elif ch == "2":
            c = course_svc.create(input("Code: "), input("Title: "), int(input("Credits: ")))
            print("Course created:", c)
        elif ch == "3":
            sid = input("Student ID: ")
            cid = input("Course ID: ")
            sem = input("Semester: ")
            e = enroll_svc.enroll(sid, cid, sem)
            print("Enrolled:", e)
        elif ch == "4":
            eid = input("Enrollment ID: ")
            score = float(input("Score: "))
            letter = input("Grade letter: ")
            g = grade_svc.add_grade(eid, score, letter)
            print("Grade recorded:", g)
        elif ch == "5":
            print(student_svc.list())
        elif ch == "6":
            print(course_svc.list())
        elif ch == "7":
            sid = input("Student ID: ")
            print(enroll_svc.list_by_student(sid))
        elif ch == "8":
            sid = input("Student ID: ")
            print(grade_svc.list_by_student(sid))
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
