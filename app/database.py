import sqlite3


class Conexao:

    def __init__(self, db_nome):
        try:
            self.conn = sqlite3.connect(db_nome)
        except Exception as erro:
            print(erro)
        else:
            self.cursor = self.conn.cursor()

    def inserir_reserva(self, reserva):
        print(self.conn)
        if self.conn:
            self.cursor.execute("""INSERT INTO RESERVAS (dono, sala, data, horario)
								   VALUES (?, ?, ?, ?)""",
                                (reserva.dono.nome, reserva.sala.numero, reserva.data, reserva.horario))
            self.salvar_alteracoes()

    def consultar_reserva(self, dono, data):
        result = self.cursor.execute("""SELECT * FROM RESERVAS WHERE dono = ? AND data = ?""",
                                     (dono, data)).fetchall()
        return result if len(result) > 0 else print(f"\n[ ! ] {nome} não possui reservas para este dia.")

    def alterar_nome(self, novo_dono, dono, sala, data, horario):
        if self.conn:
            self.cursor.execute("""UPDATE RESERVAS SET dono = ? WHERE dono = ? AND sala = ? AND data = ?
                                AND horario = ?""",
                                (novo_dono, dono, sala, data, horario))
            self.salvar_alteracoes()
            result = self.cursor.execute("""SELECT * FROM RESERVAS WHERE dono = ? AND sala = ? AND data = ?
                                            AND horario = ?""",
                                         (novo_dono, sala, data, horario)).fetchall()
            return True if result is not None else False

    def alterar_horario(self, novo_horario, dono, sala, data, horario):
        if self.conn:
            self.cursor.execute("""UPDATE RESERVAS SET horario = ? WHERE dono = ? AND sala = ? AND data = ? 
                                   AND horario = ?""",
                                (novo_horario, dono, sala, data, horario))
            self.salvar_alteracoes()
            result = self.cursor.execute("""SELECT * FROM RESERVAS WHERE dono = ? AND sala = ? AND data = ?
                                            AND horario = ?""",
                                         (dono, sala, data, novo_horario)).fetchall()
            return True if result is not None else False

    def remover_reserva(self, dono, sala, data, horario):
        if self.conn:
            self.cursor.execute("""DELETE FROM RESERVAS WHERE dono = ? AND sala = ? AND data = ? and horario = ?""",
                                (dono, sala, data, horario))
            result = self.cursor.execute("""SELECT * FROM RESERVAS WHERE dono = ? AND sala = ? AND data = ?
                                                        AND horario = ?""",
                                         (dono, sala, data, horario)).fetchall()
            if len(result) > 0:
                print("\n[ ! ] Falha ao deletar")
            else:
                self.salvar_alteracoes()
                print("\n[ + ] Deletado com sucesso!")

    def salvar_alteracoes(self):
        if self.conn:
            self.conn.commit()
