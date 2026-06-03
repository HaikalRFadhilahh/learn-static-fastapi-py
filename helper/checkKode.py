# LIBRARY
from data.data import Data
from typing import List
from dto.error import DataValidationError

# Helper
def checkKodeProgramStudi(data: str | List[str],kodeProgramStudi: list[str]) -> tuple[List[DataValidationError],bool]:
    lowerKodeProgramStudi: List[str] = [x.lower() for x in kodeProgramStudi]
    if isinstance(data,str):
        return [] if data.lower() in lowerKodeProgramStudi else [DataValidationError(field="body.kodeProgramStudi",err="Kode Program Studi is Exist")],data.lower() in lowerKodeProgramStudi
    else:
        rtnErr:List[DataValidationError] = []
        for i,d in enumerate(data):
            if d.lower() in lowerKodeProgramStudi:
                rtnErr.append(DataValidationError(field=f"body.{i}.kodeProgramStudi",err="Kode Program Studi is Exist"))
        
        return rtnErr,True if len(rtnErr) > 0 else False