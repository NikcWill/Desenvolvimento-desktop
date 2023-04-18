import sqlite3

from BlocoDeNotas.model.Nota import Nota


class DataBase:
    def __init__(self, nome ='systemBloco1.db'):
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
            TEXTO TEXT,
            DATA DATE
            );""")
        self.close_connection()

    def registrar_nota(self, nota):
        self.connect()
        curso = self.connection.cursor()
        campos_nota = ( 'TITULO', 'TEXTO', 'DATA')
        valores = f"'{nota.titulo}', '{nota.texto}', '{nota.data}'"

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

    def atualizar_nota(self, nota = Nota):
        self.connect()
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"""UPDATE NOTA SET
                            ID = '{nota.id}', 
                            TITULO = '{nota.titulo}', 
                            TEXTO = '{nota.texto}', 
                            DATA = '{nota.data}'""")

            self.connection.commit()
            return 'ok'
        except sqlite3.Error as e:
            return e
        finally:
            self.close_connection()