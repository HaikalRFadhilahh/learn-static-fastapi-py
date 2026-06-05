# LIBRARY
from fastapi import FastAPI,status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import Response
from routes.universitas import universitasRouter
from routes.programStudi import programStudiRouter
from routes.mahasiswa import mahasiswaRouter
from pydantic import ValidationError
from error.validationError import validationErrorHandler

# INIT
app = FastAPI()

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
    
# ERROR HANDLER
app.exception_handler(ValidationError)(validationErrorHandler)
app.exception_handler(RequestValidationError)(validationErrorHandler)
