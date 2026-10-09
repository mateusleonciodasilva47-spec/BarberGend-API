from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from database import SessionLocal
from models import Servico

router = APIRouter(prefix="/api/servicos", tags=["Serviços"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ServicoCreate(BaseModel):
    nome: str
    preco: int
    duracao_minutos: int | None = None

@router.post("/")
def criar_servico(servico: ServicoCreate, db: Session = Depends(get_db)):
    db_servico = Servico(**servico.dict())
    db.add(db_servico)
    db.commit()
    db.refresh(db_servico)
    return db_servico

@router.get("/")
def listar_servicos(db: Session = Depends(get_db)):
    return db.query(Servico).all()