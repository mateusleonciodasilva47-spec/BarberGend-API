from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from database import SessionLocal
from models import Barbeiro

router = APIRouter(prefix="/api/barbeiros", tags=["Barbeiros"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class BarbeiroCreate(BaseModel):
    nome: str
    especialidade: str | None = None
    disponivel: str = "sim"

@router.post("/")
def criar_barbeiro(barbeiro: BarbeiroCreate, db: Session = Depends(get_db)):
    db_barbeiro = Barbeiro(**barbeiro.dict())
    db.add(db_barbeiro)
    db.commit()
    db.refresh(db_barbeiro)
    return db_barbeiro

@router.get("/")
def listar_barbeiros(db: Session = Depends(get_db)):
    return db.query(Barbeiro).all()