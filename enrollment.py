from utils import generate_id, now_str
import database as db

class EnrollmentService:
    def enroll(self, student_id, course_id, semester):
        eid = generate_id("ENR")
        db.execute("INSERT INTO enrollments VALUES(?,?,?,?,?,?)",
                   (eid, student_id, course_id, semester, "enrolled", now_str()))
        return db.fetch("SELECT * FROM enrollments WHERE enroll_id=?", (eid,))[0]

    def withdraw(self, enroll_id):
        db.execute("UPDATE enrollments SET status='withdrawn' WHERE enroll_id=?", (enroll_id,))

    def list_by_student(self, student_id):
        return db.fetch("SELECT * FROM enrollments WHERE student_id=?", (student_id,))
