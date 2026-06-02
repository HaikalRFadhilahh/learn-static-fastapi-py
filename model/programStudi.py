# LIBRARY
from pydantic import BaseModel,Field
from typing import Literal

# Models
class ProgramStudi(BaseModel):
    kodeProgramStudi: str = Field(min_length=2,max_length=10)
    namaProgramStudi: str = Field(min_length=3,max_length=100)
    akreditasi: Literal["Unggul","A","Baik Sekali","Baik","Cukup","Belum Akreditasi"] = Field(default="Belum Akreditasi")

