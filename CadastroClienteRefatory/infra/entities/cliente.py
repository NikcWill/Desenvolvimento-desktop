from infra.configs.base import Base
from sqlalchemy import Column, String

class Cliente(Base):

    __tablename__ = 'cadastroCliente'

    cpf = Column(String(15),primary_key=True)
    nome = Column(String(100), nullable=False)
    telefone_fixo = Column(String(15), nullable=False)
    telefone_celular = Column(String(15), nullable=False)
    sexo = Column(String(100), nullable=False)
    cep = Column(String(15), nullable=False)
    logradouro = Column(String(100), nullable=False)
    numero = Column(String(7), nullable=False)
    complemento = Column(String(100), nullable=False)
    bairro = Column(String(100), nullable=False)
    municipio = Column(String(100), nullable=False)
    estado = Column(String(100), nullable=False)

    def __repr__(self):
        return f'CPF da nota = {self.cpf}, Nome = {self.nome}, Telefone fixo = {self.telefone_fixo},' \
               f'Telefone celular = {self.telefone_celular}, Sexo = {self.sexo}, CEP = {self.cep},' \
               f'Logradouro = {self.logradouro}, Numero = {self.numero}, Complemento = {self.complemento},' \
               f'Bairro = {self.bairro}, Municipio = {self.municipio}, Estado = {self.estado}'
