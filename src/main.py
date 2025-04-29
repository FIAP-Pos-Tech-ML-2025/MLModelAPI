from fastapi import FastAPI
from src.config import settings
from src.api.routes import ml_bp
from src.utils import get_logger

logger = get_logger(__name__)

def create_app():
    app = FastAPI(title=settings.APP_NAME)
    app.include_router(ml_bp, prefix="/ml")
    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)