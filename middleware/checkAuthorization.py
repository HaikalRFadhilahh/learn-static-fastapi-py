# LIBRARY
from fastapi import Request,Response,status
from fastapi.responses import JSONResponse
from starlette.middleware.base import RequestResponseEndpoint
from dto.error import DataValidationError

# Middleware 
async def checkAuthorization(r: Request,call_next: RequestResponseEndpoint) -> Response:
    token:str = r.headers.get("Authorization") or ""
    print(token)
    if token == "admin123":
        return await call_next(r)
    
    return JSONResponse(status_code=status.HTTP_403_FORBIDDEN,content={
        "status" : "error",
        "message" : "Forbidden",
        "error" : [
            DataValidationError(field="headers.Authorization",err="Invalid Token Authorization").model_dump()
        ]
    })