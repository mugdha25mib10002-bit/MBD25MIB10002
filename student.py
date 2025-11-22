
from utils import generate_id, now_str
import database as db

class StudentService:
    def create(self, name, dob, email, phone):
        sid = generate_id("STU")
        db.execute("INSERT INTO students VALUES(?,?,?,?,?,?)",
                   (sid, name, dob, email, phone, now_str()))
        return db.fetch("SELECT * FROM students WHERE student_id=?", (sid,))[0]

    def list(self):
        return db.fetch("SELECT * FROM students")

    def get(self, student_id):
        r = db.fetch("SELECT * FROM students WHERE student_id=?", (student_id,))
        return r[0] if r else None