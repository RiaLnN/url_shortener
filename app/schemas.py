from pydantic import BaseModel, HttpUrl

class URLBase(BaseModel):
    long_url: HttpUrl

class URLCreate(URLBase):
    pass

class URLResponse(BaseModel):
    short_url: str
    clicks_count: int

