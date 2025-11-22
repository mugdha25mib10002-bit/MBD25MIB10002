

import sqlite3
from pathlib import Path

DB_PATH = Path("data/sms.db")
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS users(
        username TEXT PRIMARY KEY,
        password TEXT,
        role TEXT
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS students(
        student_id TEXT PRIMARY KEY,
        name TEXT,
        dob TEXT,
        email TEXT,
        phone TEXT,
        created_at TEXT
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS courses(
        course_id TEXT PRIMARY KEY,
        code TEXT,
        title TEXT,
        credits INTEGER,
        created_at TEXT
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS enrollments(
        enroll_id TEXT PRIMARY KEY,
        student_id TEXT,
        course_id TEXT,
        semester TEXT,
        status TEXT,
        created_at TEXT,
        FOREIGN KEY(student_id) REFERENCES students(student_id),
        FOREIGN KEY(course_id) REFERENCES courses(course_id)
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS grades(
        grade_id TEXT PRIMARY KEY,
        enroll_id TEXT,
        score REAL,
        grade_letter TEXT,
        created_at TEXT,
        FOREIGN KEY(enroll_id) REFERENCES enrollments(enroll_id)
    )""")

    # insert default users (if not exists)
    c.execute("SELECT COUNT(*) as cnt FROM users")
    if c.fetchone()["cnt"] == 0:
        c.execute("INSERT INTO users(username,password,role) VALUES(?,?,?)", ("admin","admin123","admin"))
        c.execute("INSERT INTO users(username,password,role) VALUES(?,?,?)", ("staff","staff123","staff"))

    conn.commit()
    conn.close()

def fetch(query, params=()):
    conn = get_conn()
    c = conn.cursor()
    c.execute(query, params)
    rows = c.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def execute(query, params=()):
    conn = get_conn()
    c = conn.cursor()
    c.execute(query, params)
    conn.commit()
    conn.close()