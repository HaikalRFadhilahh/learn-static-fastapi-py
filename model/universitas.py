# LIBRARY
from pydantic import BaseModel,Field,ConfigDict
from typing import Literal,List
from .programStudi import ProgramStudi

class Universitas(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid"
    )
    kodeUniversitas: str = Field(min_length=3,max_length=10)
    namaUniversitas: str = Field(min_length=3)
    akreditasi: Literal["Unggul","A","Baik Sekali","Baik","Cukup","Belum Akreditasi"] = Field(default="Belum Akreditasi")
    alamat: str = Field(min_length=3)
    programStudi: List[ProgramStudi] | None = Field(default=None)
