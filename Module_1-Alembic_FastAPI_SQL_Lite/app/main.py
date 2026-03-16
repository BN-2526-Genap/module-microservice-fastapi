from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select

from .database import create_db_and_tables, get_session
from .models import User
from .schemas import UserCreate, UserRead


app = FastAPI(title="Module FastAPI - Microservice S1")


@app.on_event("startup")
def on_startup() -> None:
    create_db_and_tables()


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.post("/users", response_model=UserRead)
def create_user(
    user_in: UserCreate, session: Session = Depends(get_session)
) -> UserRead:
    user = User.from_orm(user_in)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@app.get("/users", response_model=list[UserRead])
def list_users(session: Session = Depends(get_session)) -> list[UserRead]:
    users = session.exec(select(User)).all()
    return users


@app.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int, session: Session = Depends(get_session)) -> UserRead:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
