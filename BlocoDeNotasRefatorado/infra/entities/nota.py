from infra.configs.base import Base
from sqlalchemy import Column, String, Integer,DateTime

class Nota(Base):
    __tablename__ = 'nota'

    id = Column(Integer, autoincrement=True, primary_key=True)
    titulo = Column(String(100), nullable=False)
    texto = Column(String(100), nullable=False)
    data = Column(DateTime)

    def __repr__(self):
        return f'Título da nota = {self.titulo}, id = {self.id}'