from sqlalchemy import Column, String, Integer, Date
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///para_fazer.db")
session = sessionmaker(bind=engine)()

Base = declarative_base()

class ParaFazer(Base):
    id          = Column(Integer, primary_key=True)
    titulo      = Column(String(50))
    descricao   = Column(String(200))
    dt_criacao  = Column(Date)
    concluido   = Column(Integer(1))

    def __init__(self,titulo,descricao,dt_criacao,concluido):
        self.titulo     = titulo
        self.descricao  = descricao
        self.dt_criacao = dt_criacao
        self.concluido  = concluido 

lista = ParaFazer()