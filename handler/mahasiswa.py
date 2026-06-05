# LIBRARY
from typing import Annotated
from fastapi import Query,Response, UploadFile,status,Path,Form,File
from model.mahasiswa import Mahasiswa
from data.data import DataMahasiswa,Data
from typing import List
from fastapi.responses import JSONResponse
from dto.mahasiswa import InsertMahasiswa
from dto.error import DataValidationError
from model.universitas import Universitas
from pathlib import Path as OSPath
import os

# HANDLER
async def getAllMahasiswa(q: Annotated[str | None,Query()] = None) -> Response:
    q = q if q is not None else ""
    data: List[Mahasiswa] = [d for d in DataMahasiswa if (q.lower() in d.npm.lower() or q.lower() in d.namaMahasiswa.lower() or q.lower() in d.domisili.lower())]
    return JSONResponse(
        status_code=status.HTTP_200_OK if len(data) > 0 else status.HTTP_404_NOT_FOUND,
        content={"status" : "success","message" : "Data Mahasiswa","data" : [d.model_dump() for d in data]} if len(data) > 0 else {"status" : "error","message" : "Data Mahasiswa Not Found!"}
    )

async def getDetailMahasiswa(npm: Annotated[str,Path(min_length=10,max_length=10)]) -> Response:
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
    
async def insertMahasiswa(data: Annotated[InsertMahasiswa,Form()]) -> Response:
    universitas:List[Universitas] = [x for x in Data if x.kodeUniversitas.lower() == data.kodeUniversitas.lower()]
    mahasiswa:List[Mahasiswa] = [x for x in DataMahasiswa if x.npm.lower() == data.npm.lower()]
    if len(universitas) == 0:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content={
            "status" : "error",
            "message" : "Not Found!",
            "error": [
                DataValidationError(field="body.kodeUniversitas",err="Kode Universitas Not Found!").model_dump()
            ]
        })
    
    if len(mahasiswa) > 0:
        return JSONResponse(status_code=status.HTTP_409_CONFLICT,content={
            "status" : "error",
            "message" : "Conflict!",
            "error": [
                DataValidationError(field="body.npm",err="NPM Mahasiswa is Exist!").model_dump()
            ]
        })
    
    newDataMhs:Mahasiswa = Mahasiswa(namaMahasiswa=data.namaMahasiswa,angkatan=data.angkatan,npm=data.npm,domisili=data.domisili,universitas=universitas[0])
    DataMahasiswa.append(newDataMhs)
    
    return JSONResponse(status_code=status.HTTP_200_OK,content={
        "status" : "success",
        "message" : "Success Insert Data Mahasiswa",
        "data": newDataMhs.model_dump()
    })
    
async def deleteMahasiswa(npm: Annotated[str,Path()]) -> Response:
    mhs:List[Mahasiswa] = [x for x in DataMahasiswa if x.npm.lower() == npm.lower()]
    if len(mhs) == 0:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content={
            "status" : "error",
            "message" : "Not Found!",
            "error" : [
                DataValidationError(field="path.npm",err="Data Mahasiswa Not Found!").model_dump()
            ]
        })   
        
    DataMahasiswa.remove(mhs[0])
    
    return JSONResponse(status_code=status.HTTP_200_OK,content={
        "status" : "success",
        "message" : "Data Mahasiswa Success Deleted!",
        "data" : mhs[0].model_dump()
    })
    
async def uploadFotoMahasiswa(npm: Annotated[str,Form(min_length=10,max_length=10)],foto: Annotated[UploadFile,File()]) -> Response:
    # SETTING PATH
    pathFolder:str = "public/image"
    folderUpload:OSPath = OSPath(pathFolder)
    fileUpload:OSPath = folderUpload.joinpath(f"{npm}.jpg")
    fileIsExist:bool = fileUpload.exists()
    
    # CHECK DATA MHS
    if len([x for x in DataMahasiswa if x.npm.lower() == npm.lower()])  == 0:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,content={
            "status" : "error",
            "message" : "Not Found!",
            "error" : [
                DataValidationError(field="body.npm",err="Data Mahasiswa Not Found!").model_dump()
            ]
        })
    
    # Create Folders To Upload
    folderUpload.mkdir(parents=True,exist_ok=True)
    
    # Check File
    if fileIsExist:
        fileUpload.unlink()
    
    fileUpload.touch()
    fileUpload.write_bytes(await foto.read())
    
    return JSONResponse(status_code=status.HTTP_200_OK,content={
        "status" : "success",
        "message" : "Success " + ("Updated" if fileIsExist else "Created") + " File Foto Mahasiswa",
        "data" : pathFolder + f"{npm}.jpg"
    })