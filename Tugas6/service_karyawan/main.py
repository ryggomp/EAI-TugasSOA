from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory database
karyawan_db = []

class Karyawan(BaseModel):
    id: int
    nama: str
    posisi: str
    gaji: float

@app.get("/karyawan", response_model=List[Karyawan])
def get_karyawan():
    return karyawan_db

@app.post("/karyawan", response_model=Karyawan)
def add_karyawan(karyawan: Karyawan):
    karyawan_db.append(karyawan)
    return karyawan

@app.get("/karyawan/{karyawan_id}", response_model=Karyawan)
def get_karyawan_by_id(karyawan_id: int):
    for karyawan in karyawan_db:
        if karyawan.id == karyawan_id:
            return karyawan
    return {"error": "Karyawan not found"}
