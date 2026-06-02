# LIBRARY
from fastapi.responses import JSONResponse
from fastapi import Query,Path,Body
from data.data import Data
from typing import Annotated,List,Any
from model.universitas import Universitas
from dto.universitas import UpdateUniversitas,InsertUniversitas

# HANDLER
async def getUniversitas(q: Annotated[str | None,Query()] = None) -> JSONResponse:
    filterData:List[Universitas] = []
    if q is not None:
        for d in Data:
            if str(q).lower() in d.namaUniversitas.lower() or str(q).lower() in d.akreditasi.lower() or str(q).lower() in d.kodeUniversitas.lower():
                filterData.append(d)
        
        return JSONResponse(
            status_code=200,
            content={
                "status" : "success",
                "message" : "Data Universitas",
                "data" : [x.model_dump() for x in filterData]
            }
        )
    
    return JSONResponse(status_code=200,
            content={
                "status" : "success",
                "message" : "Data Universitas",
                "data" : [x.model_dump() for x in Data]
            })

async def getDetailUniversitas(kodeUniversitas: Annotated[str,Path(min_length=3,max_length=10)]) -> JSONResponse:
    for d in Data:
        if kodeUniversitas.lower() == d.kodeUniversitas.lower():
            return JSONResponse(
                status_code=200,
                content={
                    "status" : "success",
                    "message" : "Data Detail Universitas",
                    "data" : d.model_dump()
                }
            )

    return JSONResponse(
        status_code=404,
        content={
            "status" : "error",
            "message" : "Data Universitas Not Found"
        }
    )

async def insertUniversitas(data: Annotated[InsertUniversitas,Body()]) -> JSONResponse:
    for d in Data:
        if d.kodeUniversitas.lower() == data.kodeUniversitas.lower():
            return JSONResponse(
                status_code=409,
                content={
                    "status" : "error",
                    "message" : "Conflict",
                    "error" : "Kode Universitas Exist!"
                }
            )
    Data.append(data)

    return JSONResponse(
        status_code=200,
        content={
            "status" : "error",
            "message" : "Success Add Universitas",
            "data" : data.model_dump()
        }
    )


async def updateUniversitas(kodeUniversitas: Annotated[str,Path()],dataUniversitas: Annotated[UpdateUniversitas,Body()]) -> JSONResponse:
    for i,d in enumerate(Data):
        temp:dict[str,Any] = {}
        if d.kodeUniversitas.lower() == kodeUniversitas.lower():
            temp["kodeUniversitas"] = dataUniversitas.kodeUniversitas if "kodeUniversitas" in dataUniversitas.model_fields_set else  d.kodeUniversitas
            temp["namaUniversitas"] = dataUniversitas.namaUniversitas if "namaUniversitas" in dataUniversitas.model_fields_set else  d.namaUniversitas
            temp["akreditasi"] = dataUniversitas.akreditasi if "akreditasi" in dataUniversitas.model_fields_set else  d.akreditasi
            temp["alamat"] = dataUniversitas.alamat if "alamat" in dataUniversitas.model_fields_set else  d.alamat
            
            validateRequest = Universitas.model_validate(temp)
            print(validateRequest)
            d.kodeUniversitas = validateRequest.kodeUniversitas
            d.namaUniversitas = validateRequest.namaUniversitas
            d.akreditasi = validateRequest.akreditasi
            d.alamat = validateRequest.alamat

            return JSONResponse(status_code=200,content={
                "status" : "success",
                "message" : f"Data with kode {kodeUniversitas} success Updated!",
                "data" : d.model_dump()
            })

        if i == len(Data) - 1:
            return JSONResponse(
                status_code=404,
                content={
                    "status" : "error",
                    "message" : f"Data Universitas with kode {kodeUniversitas} Not Found!"
                }
            )

async def deleteUniversitas(kodeUniversitas: Annotated[str,Path()]) -> JSONResponse:
    for i,d in enumerate(Data):
        if d.kodeUniversitas.lower() == kodeUniversitas.lower():
            Data.remove(d)
            break
            
        if i == len(Data) - 1:
            return JSONResponse(status_code=400,content={
                "status" : "error",
                "message" : f"Data Universitas with Kode {kodeUniversitas} Not Found!"
            })
        

    return JSONResponse(
        status_code=200,
        content={
            "status" : "success",
            "Message" : f"Data with Kode Universitas {kodeUniversitas} Success Deleted!"
        }
    )