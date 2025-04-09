from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory database
payroll_db = []

class Payroll(BaseModel):
    id: int
    karyawan_id: int
    bulan: str
    total_gaji: float

@app.get("/payroll/{employeeId}", response_model=List[Payroll])
def get_payroll_by_employee(employeeId: int):
    result = [payroll for payroll in payroll_db if payroll.karyawan_id == employeeId]
    if not result:
        raise HTTPException(status_code=404, detail="Payroll not found for this employee")
    return result

@app.post("/payroll", response_model=Payroll)
def process_payroll(payroll: Payroll):
    payroll_db.append(payroll)
    return payroll
