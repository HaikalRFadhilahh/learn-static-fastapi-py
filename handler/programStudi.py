# LIBRARY
from typing import Annotated, List
from fastapi import Query,Path,Body
from model.programStudi import ProgramStudi
from model.universitas import Universitas
from fastapi.responses import JSONResponse
from data.data import Data
from helper.checkKode import checkKodeProgramStudi

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
    
def insertProgramStudi(kodeUniversitas: Annotated[str,Path()],data: Annotated[ProgramStudi | List[ProgramStudi],Body()]) -> JSONResponse:
    dataUniversitas: Universitas | None = None
    for d in Data:
        if d.kodeUniversitas.lower() == kodeUniversitas.lower():
            dataUniversitas = d 
            break

    if dataUniversitas is None:
        return JSONResponse(
            status_code=404,
            content={"status" : "error","message" : f"Kode Universitas {kodeUniversitas} Not Found!"}
        )
    dkps: List[ProgramStudi] = d.programStudi if d.programStudi is not None else [] 
    dataKodeProgramStudi:List[str] = [ps.kodeProgramStudi for ps in dkps]
    if isinstance(data,ProgramStudi):
        dataErr, kodeIsExist = checkKodeProgramStudi(data.kodeProgramStudi,dataKodeProgramStudi)
        if kodeIsExist:
            return JSONResponse(
                status_code=409,
                content={
                    "status" : "error",
                    "message" : "Conflict Data kodeProgramStudi",
                    "error" : [x.model_dump() for x in dataErr]
                }
            )
        else:
            d.programStudi = d.programStudi if d.programStudi is not None else []
            d.programStudi.append(data)
            return JSONResponse(status_code=200,content={
                "status" : "success",
                "message" : f"Insert Data Program Studi in Universitas with Kode Universitas {kodeUniversitas}",
                "data" : data.model_dump()
            })
    else:
        dataErr, kodeIsExist = checkKodeProgramStudi([x.kodeProgramStudi for x in data],dataKodeProgramStudi)
        if kodeIsExist:
            return JSONResponse(
                status_code=409,
                content={
                    "status" : "error",
                    "message" : "Conflict Data kodeProgramStudi",
                    "error" : [x.model_dump() for x in dataErr]
                }
            )
        else:
            d.programStudi = d.programStudi if d.programStudi is not None else []
            for ps in data:
                d.programStudi.append(ps)
            return JSONResponse(status_code=200,content={
                "status" : "success",
                "message" : f"Insert Data Program Studi in Universitas with Kode Universitas {kodeUniversitas}",
                "data" : [x.model_dump() for x in data]
            })


def deleteProgramStudi(kodeUniversitas: Annotated[str,Path()],kodeProgramStudi: Annotated[str,Path()]) -> JSONResponse:
    for i,d in enumerate(Data):
        if d.kodeUniversitas.lower() == kodeUniversitas.lower():
            if d.programStudi is not None:
                for ps in d.programStudi:
                    if ps.kodeProgramStudi.lower() == kodeProgramStudi.lower():
                        d.programStudi.remove(ps)
                        return JSONResponse( 
                            status_code=200,
                            content={
                                "status" : "success",
                                "message" : f"Data Program Studi with Kode Universitas {kodeUniversitas} and Kode Program Studi {kodeProgramStudi} success Deleted!"
                            }
                        )
    return JSONResponse(
        status_code=404,
        content={
            "status" : "error",
            "message" : f"Data Program Studi with Kode {kodeProgramStudi} in Kode Universitas {kodeUniversitas} Not Found!"
        }
    )