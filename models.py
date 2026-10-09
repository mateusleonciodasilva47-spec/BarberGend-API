from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    telefone = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=True)

class Barbeiro(Base):
    __tablename__ = "barbeiros"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    especialidade = Column(String)
    disponivel = Column(String, default="sim")

class Servico(Base):
    __tablename__ = "servicos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    preco = Column(Integer, nullable=False)
    duracao_minutos = Column(Integer)

class Agendamento(Base):
    __tablename__ = "agendamentos"
    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer)
    barbeiro_id = Column(Integer)
    servico_id = Column(Integer)
    data_hora = Column(String, nullable=False)
    status = Column(String, default="agendado")