from fastapi import APIRouter, HTTPException
from src.ml_client import ml_client

ml_bp = APIRouter()

@ml_bp.post("/predict")
async def predict(data: dict):
    try:
        result = await ml_client.score(data)
        return {"prediction": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))