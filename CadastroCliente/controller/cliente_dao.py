import sqlite3

from CadastroCliente.model import cliente

class DataBase:
    def __init__(self, nome = 'system.db'):
        self.connection = None
        self.name = nome

    def connection(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except sqlite3.Error as e:
            print(e)

    def create_table_cliente(self):
        self.connection()
        cursor = self.connection.cursor()
        cursor.execute(
            """"
            CREATE TABLE IF NOT EXISTS CLIENTE(
            CPF TEXT,
            NOME TEXT,
            TELEFONE_FIXO TEXT,
            TELEFONE_CELULAR TEXT,
            SEXO TEXT,
            CEP TEXT,
            LOGRADOURO TEXT,
            NUMERO TEXT,
            COMPLEMENTO TEXT,
            BAIRRO TEXT,
            MUNICIPIO TEXT,
            ESTADO TEXT,
                        
            PRIMARY KEY (CPF)
            );
            """)
        self.close_connection()

    def registrar_cliente(self, cliente):
        self.connect()
        curso = self.connection.cursor()
        campos_cliente = ('CPF', 'NOME', 'TELEFONE_FIXO', 'TELEFONE_CELULAR',
                          'SEXO', 'CEP', 'LOGRADOURO', 'NUMERO', 'COMPLEMENTO',
                          'BAIRRO','MUNICIPIO', 'ESTADO')
        valores = f"'{str(cliente.cpf).replace('.','').replace('-','')}', '{cliente.nome}', " \
                  f"'{cliente.telefone_fixo}', '{cliente.telefone_celular}', '{cliente.sexo}', " \
                  f"'{cliente.cep}', '{cliente.logradouro}', '{cliente.numero}', '{cliente.complemento}', " \
                  f"'{cliente.bairro}', '{cliente.municipio}', '{cliente.estado}'"
        try:
            curso.execute(f""" INSERT INTO CLIENTE {campos_cliente} VALUES ({valores})""")
            self.connection.commit()
            return
        except sqlite3.Error as e:
            print(e)
        finally:
            self.close_connection()