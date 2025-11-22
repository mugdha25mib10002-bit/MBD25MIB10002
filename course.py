from utils import generate_id, now_str
import database as db

class CourseService:
    def create(self, code, title, credits):
        cid = generate_id("CRS")
        db.execute("INSERT INTO courses VALUES(?,?,?,?,?)",
                   (cid, code, title, credits, now_str()))
        return db.fetch("SELECT * FROM courses WHERE course_id=?", (cid,))[0]

    def list(self):
        return db.fetch("SELECT * FROM courses")

    def get(self, course_id):
        r = db.fetch("SELECT * FROM courses WHERE course_id=?", (course_id,))
        return r[0] if r else None