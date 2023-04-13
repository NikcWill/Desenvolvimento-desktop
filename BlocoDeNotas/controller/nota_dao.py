import sqlite3

from BlocoDeNotas.model.nota import Nota


class DataBase:
    def __init__(self, nome ='systemBloco.db'):
        self.connection = None
        self.name = nome

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except sqlite3.Error as e:
            print(e)

    def criar_tabela_notas(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS NOTA(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            TITULO TEXT,
            DATA DATE,
            TEXTO TEXT
            );""")
        self.close_connection()

    def registrar_nota(self, nota):
        self.connect()
        curso = self.connection.cursor()
        campos_nota = ('ID', 'TITULO', 'DATA', 'TEXTO')
        valores = f"'{nota.id}', '{nota.titulo}', '{nota.data}', {nota.texto}"

        try:
            curso.execute(f""" INSERT INTO NOTA {campos_nota} VALUES ({valores})""")
            self.connection.commit()
            return 'ok'
        except sqlite3.Error as e:
            return str(e)
        finally:
            self.close_connection()

    def consultar_nota(self, id):
        self.connect()
        try:
            cursor = self.connection.cursor()
            cursor.execute(f""" SELECT * FROM NOTA WHERE ID = '{id}'""")
            return cursor.fetchone()
        except sqlite3.Error as e:
            return e
        finally:
            self.close_connection()

    def consultar_todas_notas(self):
        self.connect()
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM NOTA")
            notas = cursor.fetchall()
            return notas
        except sqlite3.Error as e:
            print(f'Erro {e}')
            return None
        finally:
            self.close_connection()

    def deletar_nota(self, id):
        self.connect()
        try:
            cursor = self.connection.cursor()
            cursor.execute(f""" DELETE FROM NOTA FROM NOTA WHERE ID = '{id}'""")
            self.connection.commit()
            return 'ok'
        except sqlite3.Error as e:
            return e
        finally:
            self.close_connection()

    def atualizar_cliente(self, nota = Nota):
        self.connect()
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"""UPDATE NOTA SET
                            ID = '{nota.id}', 
                            TITULO = '{nota.titulo}', 
                            DATA = '{nota.data}', 
                            TEXTO = '{nota.texto}'""")

            self.connection.commit()
            return 'ok'
        except sqlite3.Error as e:
            return e
        finally:
            self.close_connection()