# LIBRARY
from typing import Annotated
from fastapi import Query,Response,status,Path
from model.mahasiswa import Mahasiswa
from data.data import DataMahasiswa
from typing import List
from fastapi.responses import JSONResponse

# HANDLER
async def GetAllMahasiswa(q: Annotated[str | None,Query()] = None) -> Response:
    q = q if q is not None else ""
    data: List[Mahasiswa] = [d for d in DataMahasiswa if (q.lower() in d.npm.lower() or q.lower() in d.namaMahasiswa.lower() or q.lower() in d.domisili.lower())]
    return JSONResponse(
        status_code=status.HTTP_200_OK if len(data) > 0 else status.HTTP_404_NOT_FOUND,
        content={"status" : "success","message" : "Data Mahasiswa","data" : [d.model_dump() for d in data]} if len(data) > 0 else {"status" : "error","message" : "Data Mahasiswa Not Found!"}
    )

async def GetDetailMahasiswa(npm: Annotated[str,Path(min_length=10,max_length=10)]) -> Response:
    for d in DataMahasiswa:
        if d.npm.lower() == npm.lower():
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={
                    "status" : "success",
                    "message" : f"Data Mahasiswa with NPM {npm}",
                    "data" : d.model_dump()
                }
            )
    
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status" : "error",
            "message" : f"Data Mahasiswa with NPM {npm} Not Found!"
        }
    )