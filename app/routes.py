from fastapi import APIRouter, Depends, HTTPException
from app.services import save_url, get_url_by_hash, get_url_stats
from fastapi.responses import RedirectResponse
from app.schemas import URLCreate, URLResponse
from app.database import get_db
from typing import Annotated
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/shorten", response_model=URLResponse)
def shorten(url: URLCreate, db: Annotated[Session, Depends(get_db)]):
    db_url = save_url(url, db)
    return db_url

@router.get("/{short_url}")
def redirect_url(short_url: str, db: Annotated[Session, Depends(get_db)]):
    long_url = str(get_url_by_hash(short_url, db))
    
    if long_url is None:
        raise HTTPException(status_code=404, detail="Link not found")

    return RedirectResponse(url=long_url)

@router.get("/api/stats/{short_url}")
def get_stats(short_url: str, db: Annotated[Session, Depends(get_db)]):
    clicks_count = get_url_stats(short_url, db)

    if clicks_count is None:
        raise HTTPException(status_code=404, detail="Link not found")
    
    return {"clicks_count": clicks_count}