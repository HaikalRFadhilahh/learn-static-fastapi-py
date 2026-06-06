# LIBRARY
from fastapi import FastAPI,status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, Response
from routes.universitas import universitasRouter
from routes.programStudi import programStudiRouter
from routes.mahasiswa import mahasiswaRouter
from pydantic import ValidationError
from error.validationError import validationErrorHandler
from fastapi.staticfiles import StaticFiles
from middleware.checkAuthorization import checkAuthorization
from dotenv import load_dotenv
import os
from pathlib import Path as OSPath

# LOAD ENV
load_dotenv(override=True)

# INIT
app = FastAPI()

# Middleware
app.middleware("http")(checkAuthorization)

# INCLUDE EXTERNAL ROUTER
app.include_router(universitasRouter)
app.include_router(programStudiRouter)
app.include_router(mahasiswaRouter)

# ROOT ENDPOINT
@app.get("/")
def root() -> Response:
    return Response(
        content="Application Programming Interface build with FastAPI",
        status_code=status.HTTP_200_OK,
        headers={
            "Content-Type" : "text/plain"
        }
    )

@app.get('/health')
def health() -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status" : "success",
            "message" : "Application Running Good and Health!"
        }
    )
    
# STATIC Endpoint
OSPath("public/static").mkdir(parents=True,exist_ok=True)
app.mount("/static",StaticFiles(directory="public"))    
    
# ERROR HANDLER
app.exception_handler(ValidationError)(validationErrorHandler)
app.exception_handler(RequestValidationError)(validationErrorHandler)

# PRODUCTION
if __name__ == '__main__':
    import uvicorn
    if (os.getenv("APP_NAME") is None or os.getenv("APP_NAME") == "") or (os.getenv("APP_HOST") is None or os.getenv("APP_HOST") == "") or (os.getenv("APP_PORT") is None or os.getenv("APP_PORT") == "" or not str(os.getenv("APP_PORT")).isdigit()) or (os.getenv("APP_PORT") is None or os.getenv("APP_PORT") == "") or (os.getenv("TOKEN") is None or os.getenv("TOKEN") == ""):
        print("Error: Invalid ENV please check your .env or Read the Docs!")
    else:   
        uvicorn.run(app="main:app",host=str(os.getenv("APP_HOST")),port=int(str(os.getenv("APP_PORT"))),reload=True)
    