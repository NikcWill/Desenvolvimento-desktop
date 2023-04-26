from infra.configs.base import Base
from sqlalchemy import  Column, String, Integer,DateTime

class Nota:
    __tablename__ = 'nota'

    id = Column(Integer, autoincrement=True, primary_key=True)
    titulo = Column(String, nullable=False)
    texto = Column(String, nullable=False)
    data = Column(DateTime)

    def __repr__(self):
        return f'Título da nota = {self.titulo}, id = {self.id}'