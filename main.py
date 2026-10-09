from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="BarberGend API")

# Banco temporário em memória
clientes_db = []
barbeiros_db = []
servicos_db = []
agendamentos_db = []

# Schemas
class ClienteCreate(BaseModel):
    nome: str
    telefone: str
    email: Optional[str] = None

class BarbeiroCreate(BaseModel):
    nome: str
    especialidade: Optional[str] = None
    disponivel: str = "sim"

class ServicoCreate(BaseModel):
    nome: str
    preco: int
    duracao_minutos: Optional[int] = None

class AgendamentoCreate(BaseModel):
    cliente_id: int
    barbeiro_id: int
    servico_id: int
    data_hora: str
    status: str = "agendado"

# Rota inicial
@app.get("/")
def inicio():
    return {"mensagem": "API BarberGend funcionando!"}

# Clientes
@app.post("/api/clientes")
def criar_cliente(cliente: ClienteCreate):
    novo = {"id": len(clientes_db)+1, **cliente.dict()}
    clientes_db.append(novo)
    return novo

@app.get("/api/clientes")
def listar_clientes():
    return clientes_db

# Barbeiros
@app.post("/api/barbeiros")
def criar_barbeiro(barbeiro: BarbeiroCreate):
    novo = {"id": len(barbeiros_db)+1, **barbeiro.dict()}
    barbeiros_db.append(novo)
    return novo

@app.get("/api/barbeiros")
def listar_barbeiros():
    return barbeiros_db

# Serviços
@app.post("/api/servicos")
def criar_servico(servico: ServicoCreate):
    novo = {"id": len(servicos_db)+1, **servico.dict()}
    servicos_db.append(novo)
    return novo

@app.get("/api/servicos")
def listar_servicos():
    return servicos_db

# Agendamentos
@app.post("/api/agendamentos")
def criar_agendamento(agendamento: AgendamentoCreate):
    novo = {"id": len(agendamentos_db)+1, **agendamento.dict()}
    agendamentos_db.append(novo)
    return novo

@app.get("/api/agendamentos")
def listar_agendamentos():
    return agendamentos_db
    