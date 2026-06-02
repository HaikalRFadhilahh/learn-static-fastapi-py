# LIBRARY
from fastapi.routing import APIRouter
from handler.universitas import getUniversitas,getDetailUniversitas,deleteUniversitas,updateUniversitas,insertUniversitas

# UNIVERSITAS SUB ROUTING
universitasRouter = APIRouter(prefix="/universitas")

# Routing
universitasRouter.get("")(getUniversitas)
universitasRouter.get("/{kodeUniversitas}/detail")(getDetailUniversitas)
universitasRouter.post("")(insertUniversitas)
universitasRouter.patch("/{kodeUniversitas}")(updateUniversitas)
universitasRouter.delete("/{kodeUniversitas}")(deleteUniversitas)
