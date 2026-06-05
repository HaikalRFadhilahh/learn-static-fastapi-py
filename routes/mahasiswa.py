# LIBRARY
from fastapi.routing import APIRouter
from httpx import delete
from handler.mahasiswa import getAllMahasiswa,getDetailMahasiswa,insertMahasiswa,deleteMahasiswa,uploadFotoMahasiswa

# SUB Router
mahasiswaRouter = APIRouter(prefix="/mahasiswa")

# Route
mahasiswaRouter.get("/")(getAllMahasiswa)
mahasiswaRouter.get("/{npm}/detail")(getDetailMahasiswa)
mahasiswaRouter.post("/")(insertMahasiswa)
mahasiswaRouter.post("/upload")(uploadFotoMahasiswa)
mahasiswaRouter.delete("/{npm}")(deleteMahasiswa)