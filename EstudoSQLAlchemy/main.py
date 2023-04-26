from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
database_url = 'mysql+pymysql://root:Senac2021@localhost:3306/locadora'

class Filme(Base):
    __tablename__ = 'filme'

    id = Column(Integer, autoincrement=True, primary_key=True)
    titulo = Column(String(100), nullable=False)
    genero = Column(String(100), nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
        return f'Filme [Titulo = {self.titulo}, Gênero = {self.genero}, Ano = {self.ano}]'


def create_database():
    engine = create_engine(database_url, echo=True)
    try:
        engine.connect()
    except Exception as e:
        if '1049' in str(e):
            engine = create_engine(database_url.rsplit('/', 1)[0], echo=True)
            conn = engine.connect()
            conn.execute('CREATE DATABASE locadora')
            conn.close()
            print('Banco locadora criado com sucesso')

        else:
            raise e

create_database()

#Configurações

engine = create_engine(database_url, echo=True)
conn = engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

def create_table():
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
    print('Tabela filme criada com sucesso!')

create_table()

#adicionar no banco
data_insert = Filme(titulo = 'Emanuelle', ano = '1974', genero = 'Entreterimento')
session.add(data_insert)
session.commit()
data_insert2 = Filme(titulo = 'Batman', ano = '2006', genero = 'ação')
session.add(data_insert2)
session.commit()
data_insert3 = Filme(titulo = 'Diego e agnaldo', ano = '1974', genero = 'comedia')
session.add(data_insert3)
session.commit()

#remover do banco
session.query(Filme).filter(Filme.titulo == 'Emanuelle').delete()
session.commit()

#atualizar no banco
session.query(Filme).filter(Filme.titulo == 'Batman').update( {'titulo': 'Batíma'})
session.commit()

#consultar no banco
data =  session.query(Filme).all()

print(f'Filmes {data}')

session.close()