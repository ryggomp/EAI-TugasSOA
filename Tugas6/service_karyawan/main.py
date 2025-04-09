from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory databases
karyawan_db = []
attendance_db = []

class Karyawan(BaseModel):
    id: int
    nama: str
    posisi: str
    gaji: float

class Attendance(BaseModel):
    id: int
    karyawan_id: int
    tanggal: str
    status: str  # "Check-in" or "Check-out"

@app.get("/employees", response_model=List[Karyawan])
def get_employees():
    return karyawan_db

@app.post("/employees", response_model=Karyawan)
def add_employee(karyawan: Karyawan):
    karyawan_db.append(karyawan)
    return karyawan

@app.get("/employees/{id}", response_model=Karyawan)
def get_employee_by_id(id: int):
    for karyawan in karyawan_db:
        if karyawan.id == id:
            return karyawan
    raise HTTPException(status_code=404, detail="Employee not found")

@app.put("/employees/{id}", response_model=Karyawan)
def update_employee(id: int, updated_karyawan: Karyawan):
    for index, karyawan in enumerate(karyawan_db):
        if karyawan.id == id:
            karyawan_db[index] = updated_karyawan
            return updated_karyawan
    raise HTTPException(status_code=404, detail="Employee not found")

@app.delete("/employees/{id}")
def delete_employee(id: int):
    for index, karyawan in enumerate(karyawan_db):
        if karyawan.id == id:
            del karyawan_db[index]
            return {"message": "Employee deleted successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")
