from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String

class URLModel(Base):
    __tablename__="urls"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    long_url: Mapped[str] = mapped_column(String, nullable=False)
    short_url: Mapped[str] = mapped_column(String, unique=True, index=True, nullable=False)
    clicks_count: Mapped[int] = mapped_column(Integer, default=0)