# LIBRARY
from typing import Literal
from pydantic import BaseModel,Field

# DTO
class DTOProgramStudi(BaseModel):
    kodeProgramStudi: str = Field(min_length=2,max_length=10)
    
class UpdateProgramStudi(BaseModel):
    kodeProgramStudi: str | None = Field(default=None,min_length=2,max_length=10)
    namaProgramStudi: str | None = Field(default=None,min_length=3,max_length=100)
    akreditas: Literal["Unggul","A","Baik Sekali","Baik","Cukup","Belum Akreditasi"] | None = Field(default=None)
    
class PathUpdateProgramStudi(DTOProgramStudi):
    kodeUniversitas: str = Field(min_length=3,max_length=10)
    
