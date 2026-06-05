# LIBRARY
from pydantic import BaseModel,Field
from model.universitas import Universitas

class BaseMahasiswa(BaseModel):
    npm: str = Field(min_length=10,max_length=10)
    namaMahasiswa: str = Field(min_length=2)
    angkatan:int = Field(gt=2000)
    domisili: str = Field(min_length=1)

class Mahasiswa(BaseMahasiswa):
    universitas: Universitas = Field()

