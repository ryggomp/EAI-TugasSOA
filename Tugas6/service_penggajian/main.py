from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory database
penggajian_db = []

class Penggajian(BaseModel):
    id: int
    karyawan_id: int
    bulan: str
    total_gaji: float

@app.get("/penggajian", response_model=List[Penggajian])
def get_penggajian():
    return penggajian_db

@app.post("/penggajian", response_model=Penggajian)
def add_penggajian(penggajian: Penggajian):
    penggajian_db.append(penggajian)
    return penggajian

@app.get("/penggajian/{karyawan_id}", response_model=List[Penggajian])
def get_penggajian_by_karyawan(karyawan_id: int):
    return [penggajian for penggajian in penggajian_db if penggajian.karyawan_id == karyawan_id]
