
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from database import get_connection, create_table


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_table()
    yield


app = FastAPI(
    title="Student Management API",
    lifespan=lifespan
)


class Student(BaseModel):
    name: str
    date_of_birth: str
    email: str | None = None
    phone: str | None = None
    course: str | None = None
    address: str | None = None


# 1. Add a student
@app.post("/students")
def add_student(student: Student):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO students
        (name, date_of_birth, email, phone, course, address)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            student.name,
            student.date_of_birth,
            student.email,
            student.phone,
            student.course,
            student.address
        )
    )

    conn.commit()
    student_id = cursor.lastrowid
    conn.close()

    return {
        "message": "Student added successfully",
        "student_id": student_id
    }


# 2. Get all students
@app.get("/students")
def get_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = [dict(row) for row in cursor.fetchall()]

    conn.close()
    return students


# 3. Get one student
@app.get("/students/{student_id}")
def get_student(student_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE student_id = ?",
        (student_id,)
    )

    student = cursor.fetchone()
    conn.close()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return dict(student)


# 4. Update a student
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE students
        SET name = ?, date_of_birth = ?, email = ?,
            phone = ?, course = ?, address = ?
        WHERE student_id = ?
        """,
        (
            student.name,
            student.date_of_birth,
            student.email,
            student.phone,
            student.course,
            student.address,
            student_id
        )
    )

    conn.commit()
    updated = cursor.rowcount
    conn.close()

    if updated == 0:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {"message": "Student updated successfully"}


# 5. Delete a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM students WHERE student_id = ?",
        (student_id,)
    )

    conn.commit()
    deleted = cursor.rowcount
    conn.close()

    if deleted == 0:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return {"message": "Student deleted successfully"}
