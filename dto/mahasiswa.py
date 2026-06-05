# LIBRARY
from model.mahasiswa import BaseMahasiswa
from pydantic import Field

# DTO
class InsertMahasiswa(BaseMahasiswa):
    kodeUniversitas:str = Field(min_length=2)
    