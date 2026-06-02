# LIBRARY
from pydantic import BaseModel,Field,ConfigDict

class DataValidationError(BaseModel):
    model_config = ConfigDict(extra="forbid")
    field:str = Field()
    err: str = Field()
