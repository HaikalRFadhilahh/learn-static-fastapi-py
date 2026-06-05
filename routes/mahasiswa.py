# LIBRARY
from fastapi.routing import APIRouter
from handler.mahasiswa import GetAllMahasiswa,GetDetailMahasiswa

# SUB Router
mahasiswaRouter = APIRouter(prefix="/mahasiswa")

# Route
mahasiswaRouter.get("/")(GetAllMahasiswa)
mahasiswaRouter.get("/{npm}/detail")(GetDetailMahasiswa)