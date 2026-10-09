from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from database import SessionLocal
from models import Agendamento

router = APIRouter(prefix="/api/agendamentos", tags=["Agendamentos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class AgendamentoCreate(BaseModel):
    cliente_id: int
    barbeiro_id: int
    servico_id: int
    data_hora: str
    status: str = "agendado"

@router.post("/")
def criar_agendamento(agendamento: AgendamentoCreate, db: Session = Depends(get_db)):
    db_agendamento = Agendamento(**agendamento.dict())
    db.add(db_agendamento)
    db.commit()
    db.refresh(db_agendamento)
    return db_agendamento

@router.get("/")
def listar_agendamentos(db: Session = Depends(get_db)):
    return db.query(Agendamento).all()