from utils import generate_id, now_str
import database as db

class GradeService:
    def add_grade(self, enroll_id, score, grade_letter):
        gid = generate_id("GRD")
        db.execute("INSERT INTO grades VALUES(?,?,?,?,?)",
                   (gid, enroll_id, score, grade_letter, now_str()))
        return db.fetch("SELECT * FROM grades WHERE grade_id=?", (gid,))[0]

    def list_by_student(self, student_id):
        # join grades -> enrollments -> students
        return db.fetch("""
            SELECT g.*, e.student_id, e.course_id
            FROM grades g JOIN enrollments e ON g.enroll_id = e.enroll_id
            WHERE e.student_id=?
        """, (student_id,))