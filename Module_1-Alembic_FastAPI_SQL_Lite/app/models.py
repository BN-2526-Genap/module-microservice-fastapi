from datetime import datetime

from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, max_length=100)
    email: str = Field(index=True, unique=True, max_length=150)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
