from fastapi import FastAPI
from app.routes import router
from app.database import Base, engine
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

def get_application():
    app = FastAPI(docs_url='/docs', lifespan=lifespan)
    app.include_router(router=router)
    # future settings
    
    return app


app = get_application()