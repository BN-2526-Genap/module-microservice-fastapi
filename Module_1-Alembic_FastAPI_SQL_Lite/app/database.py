from contextlib import contextmanager
from typing import Iterator

from sqlmodel import SQLModel, create_engine, Session


DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)


@contextmanager
def get_session() -> Iterator[Session]:
    with Session(engine) as session:
        yield session
