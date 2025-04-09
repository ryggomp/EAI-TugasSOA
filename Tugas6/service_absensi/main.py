from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory database
attendance_db = []

class Attendance(BaseModel):
    id: int
    karyawan_id: int
    tanggal: str
    status: str  # "Check-in" or "Check-out"

@app.post("/attendance/check-in", response_model=Attendance)
def check_in(attendance: Attendance):
    attendance.status = "Check-in"
    attendance_db.append(attendance)
    return attendance

@app.post("/attendance/check-out", response_model=Attendance)
def check_out(attendance: Attendance):
    attendance.status = "Check-out"
    attendance_db.append(attendance)
    return attendance

@app.get("/attendance/{employeeId}", response_model=List[Attendance])
def get_attendance_history(employeeId: int):
    return [record for record in attendance_db if record.karyawan_id == employeeId]
