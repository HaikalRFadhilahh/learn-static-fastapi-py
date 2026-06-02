# LIBARY
from pydantic import BaseModel,Field,ConfigDict
from typing import Literal,List
from model.programStudi import ProgramStudi


class UpdateUniversitas(BaseModel):
    model_config = ConfigDict(extra="forbid")

    kodeUniversitas: str | None = Field(default=None,min_length=3,max_length=10)
    namaUniversitas: str | None= Field(default=None,min_length=3)
    akreditasi: Literal["Unggul","A","Baik Sekali","Baik","Cukup","Belum Akreditasi"] | None = Field(default=None)
    alamat: str | None = Field(default=None,min_length=3)

class InsertUniversitas(BaseModel):
    model_config = ConfigDict(extra="forbid")

    kodeUniversitas: str= Field(min_length=3,max_length=10)
    namaUniversitas: str= Field(min_length=3)
    akreditasi: Literal["Unggul","A","Baik Sekali","Baik","Cukup","Belum Akreditasi"] = Field(default="Belum Akreditasi")
    alamat: str = Field(min_length=3)
    programStudi: List[ProgramStudi] | None = Field(default=None)
