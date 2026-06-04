# LIBRARY
from fastapi.routing import APIRouter
from handler.programStudi import getProgramStudi,getProgramStudiUniversitas,deleteProgramStudi,insertProgramStudi,updateProgramStudi

# PROGRAM STUDI SUB ROUTER
programStudiRouter = APIRouter(prefix="/prodi")

# ROUTERS
programStudiRouter.get("")(getProgramStudi)
programStudiRouter.get("/{kodeUniversitas}/detail")(getProgramStudiUniversitas)
programStudiRouter.post("/{kodeUniversitas}")(insertProgramStudi)
programStudiRouter.patch("/{kodeUniversitas}/{kodeProgramStudi}")(updateProgramStudi)
programStudiRouter.delete("/{kodeUniversitas}/{kodeProgramStudi}")(deleteProgramStudi)