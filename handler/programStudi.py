# LIBRARY
from typing import Annotated, List
from fastapi import Query,Path
from model.programStudi import ProgramStudi
from fastapi.responses import JSONResponse
from data.data import Data


# HANDLER
def getProgramStudi(q: Annotated[str | None,Query()] = None) -> JSONResponse:
    dataProgramStudi: List[ProgramStudi] = [x for d in Data if d.programStudi is not None for x in d.programStudi] if q is None else []
    for i in Data:
        if i.programStudi is not None:
            for d in i.programStudi:
                if q is not None and (q.lower() in d.namaProgramStudi.lower() or q.lower() in d.kodeProgramStudi.lower()):
                    dataProgramStudi.append(d)
                
    return JSONResponse(
        status_code=200,
        content={
            "status": "success",
            "message" : "Data Program Studi semua Universitas",
            "data": [d.model_dump() for d in dataProgramStudi]
        }
    )
    
def getProgramStudiUniversitas(kodeUniversitas: Annotated[str,Path()],q: Annotated[str | None,Query()] = None) -> JSONResponse:
    data: List[ProgramStudi] = []
    for d in Data:
        if kodeUniversitas.lower() == d.kodeUniversitas.lower() and d.programStudi is not None:
            data = [ps for ps in d.programStudi if q is not None and (q.lower() in ps.kodeProgramStudi.lower() or q.lower() in ps.namaProgramStudi.lower())]
                
    return JSONResponse(
        status_code=200,
        content={
            "status" : "success",
            "message" : "Data Program Studi",
            "data" : [x.model_dump() for x in data]
        }
    )
    