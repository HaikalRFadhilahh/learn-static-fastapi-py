# LIBRARY
from fastapi.routing import APIRouter
from handler.programStudi import getProgramStudi,getProgramStudiUniversitas

# PROGRAM STUDI SUB ROUTER
programStudiRouter = APIRouter(prefix="/prodi")

# ROUTERS
programStudiRouter.get("")(getProgramStudi)
programStudiRouter.get("/{kodeUniversitas}")(getProgramStudiUniversitas)