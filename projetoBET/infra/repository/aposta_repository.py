from infra.configs.connection import DBConnectionHandler
from infra.entities.aposta import Aposta


class ApostaRepository:

    def select_all(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Aposta).all()
            return data

    def select(self, id):
        with DBConnectionHandler() as db:
            data = db.session.query(Aposta).filter(Aposta.id == id).first()
            return data

    def insert(self, aposta):
        with DBConnectionHandler() as db:
            try:
                db.session.add(aposta)
                db.session.commit()
                return 'ok'
            except Exception as e:
                db.session.rollback()
                return e

    def delete(self, id):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Aposta).filter(Aposta.id == id).delete()
                db.session.commit()
                return 'ok'
            except Exception as e:
                db.session.rollback()
                return e



    def update(self, aposta):
        with DBConnectionHandler() as db:

            try:
                db.session.query(Aposta).filter(Aposta.id == aposta.id) \
                    .update({'nome': aposta.nome, 'aposta_vencedor': aposta.aposta_vencedor, 'placar_casa': aposta.placar_casa,\
                             'placar_visiante ': aposta.placar_visitante, 'valor_aposta': aposta.valor_aposta, 'resultado_casa': aposta.resultado_casa,\
                             'resultado_visitante': aposta.resultado_visitante, 'valor_ganho': aposta.valor_ganho})
                db.session.commit()
                return 'ok'
            except Exception as e:
                db.session.rollback()
                return e