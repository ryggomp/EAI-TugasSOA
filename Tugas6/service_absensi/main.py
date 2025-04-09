from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory database
absensi_db = []

class Absensi(BaseModel):
    id: int
    karyawan_id: int
    tanggal: str
    status: str  # "Hadir" or "Tidak Hadir"

@app.get("/absensi", response_model=List[Absensi])
def get_absensi():
    return absensi_db

@app.post("/absensi", response_model=Absensi)
def add_absensi(absensi: Absensi):
    absensi_db.append(absensi)
    return absensi

@app.get("/absensi/{karyawan_id}", response_model=List[Absensi])
def get_absensi_by_karyawan(karyawan_id: int):
    return [absensi for absensi in absensi_db if absensi.karyawan_id == karyawan_id]
