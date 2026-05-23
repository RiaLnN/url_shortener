import secrets
from app.schemas import URLCreate, URLResponse
from sqlalchemy.orm import Session
from app.models import URLModel
from sqlalchemy import select, update


def get_random_hash_url() -> str:
    new_url =  secrets.token_urlsafe(6)
    return new_url

def save_url(url: URLCreate, db: Session) -> URLResponse:
    key = URLResponse(short_url=get_random_hash_url(), clicks_count=0)
    new_url = URLModel(
        long_url=str(url.long_url),
        short_url=key.short_url,
        )
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    
    return key

def get_url_by_hash(key: str, db: Session) -> str | None:
    res = db.execute(
        select(URLModel.long_url)
        .where(URLModel.short_url == key)
    )
    db.execute(
        update(URLModel)
        .where(URLModel.short_url == key)
        .values(clicks_count=URLModel.clicks_count + 1)
    )
    db.commit()
    return res.scalar_one_or_none()

def get_url_stats(key: str, db: Session) -> int | None:
    res = db.execute(
        select(URLModel.clicks_count)
        .where(URLModel.short_url == key)
    )
    return res.scalar_one_or_none()