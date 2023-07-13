from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, Float


class Aposta(Base):

    __tablename__ = 'betDB'

    id = Column(Integer, autoincrement=True, primary_key=True)
    nome = Column(String(100), nullable=False)
    aposta_vencedor = Column(Integer, nullable=False)
    placar_casa = Column(Integer, nullable=False)
    placar_visitante = Column(Integer, nullable=False)
    valor_aposta = Column(Float, nullable=False)
    resultado_casa = Column(String(100), nullable=False)
    resultado_visitante = Column(String(7), nullable=False)
    valor_ganho = Column(Float, nullable=False)


    def __repr__(self):
        return f'id da nota = {self.id}, Nome = {self.nome}, Aposta Vencedor = {self.aposta_vencedor},' \
               f'Placar da Casa = {self.placar_casa}, Placar do Visitante = {self.placar_visitante}, Valor Apostado = {self.valor_aposta},' \
               f'resultado Casa = {self.resultado_casa}, resultado Visitante = {self.resultado_visitante}, Valor Ganho = {self.valor_ganho},' \

