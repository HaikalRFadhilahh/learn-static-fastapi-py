# LIBRARY
from fastapi.responses import JSONResponse
from fastapi import Request
from pydantic import ValidationError
from dto.error import DataValidationError
from typing import List

async def validationErrorHandler(r: Request,error: ValidationError) ->JSONResponse:
    dataErr: List[DataValidationError] = []
    print(error.errors())
    for e in error.errors():
        print(len(e["loc"]))
        dataErr.append(DataValidationError(**{
            "field" : e["loc"][0] if e["loc"][0] not in ["query","path","body"] or len(e["loc"]) == 1 else e["loc"][1],
            "err" : e["msg"]
        }))
    return JSONResponse(
        status_code=400,
        content={
            "status" : "error",
            "message" : "Invalid Request",
            "error" : [x.model_dump() for x in dataErr]
        }
    )
    