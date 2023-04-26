from infra.configs.connection import DBCOnnectionHandler
from infra.entities.nota import Nota

class NotaRepository:
    def select(self):
        with DBCOnnectionHandler() as db:
            data = db.session.query(Nota).all()
            return data

    def insert(self, titulo, texto, data):
        with DBCOnnectionHandler() as db:
            data_insert = Nota (titulo=titulo, texto=texto, data=data)
        db.session.add(data_insert)
        db.session.commit()

    def delete(self, id):
        with DBCOnnectionHandler() as db:
            db.session.query(Nota).filter(Nota.id == id).delete()
            db.session.commit()

    def update(self, id, titulo, texto, data):
        with DBCOnnectionHandler() as db:
            db.session.query(Nota).filter(Nota.id == id)\
            .upadate({'titulo' : titulo, 'texto' : texto,})
        db.session.commit()

