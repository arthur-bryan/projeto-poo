"""
    ESTE ARQUIVO É UM MÓDULO PERTENCENTE AO PROJETO 'projeto-poo',
    DISPONÍVEL EM 'https://github.com/arthurbryan/projeto-poo'
"""

import sqlite3


class Conexao:
    """ Classe que representa a conexão com o banco de dados e realiza consultas ou alterações

        Attributes:
            self.conn (:obj: 'sqlite3.connect'): Objeto da conexão
            self.cursor (:obj: 'sqlite3.cursor') Objeto que executa consultas e alterações

    """

    def __init__(self, db_nome):
        """ Args:
                db_nome (:obj: 'str'): nome/caminho do banco de dados """
        try:
            self.conn = sqlite3.connect(db_nome)
        except Exception as erro:
            print(f"\n[ ! ] {erro}")
            self.fechar()
        else:
            self.cursor = self.conn.cursor()

    def inserir_reserva(self, reserva):
        """ Insere a reserva na tabela baseado seus atributos

            Args:
                reserva (:obj: 'Reserva'): Objeto da classe Reserva a ser inserido na tabela
        """
        self.cursor.execute("""INSERT INTO RESERVAS (dono, sala, data, horario)
							   VALUES (?, ?, ?, ?)""",
                            (reserva.dono.nome, reserva.sala.numero,
                             reserva.data, reserva.horario))
        self.salvar_alteracoes()

    def consultar_reserva(self, dono, data):
        """ Insere a reserva na tabela baseado seus atributos

            Args:
                dono (:obj: 'str'): nome do dono para verificação na consulta
                data (:obj: 'str') data a ser consultada

            Returns:
                resultados (:obj: 'list' of :obJ: 'tuple'): lista de tuplas com os resultados da
                consulta caso exista algum, False caso nenhum valor seja encontrado na consulta.
        """
        resultados = self.cursor.execute("""SELECT * FROM RESERVAS WHERE dono = ? AND data = ?""",
                                         (dono, data)).fetchall()
        return resultados if len(resultados) > 0 else False

    def alterar_nome(self, novo_dono, dono, sala, data, horario):
        """ Altera o nome do dono de uma reserva caso a reserva e o novo dono existam

            Args:
                novo_dono (:obj: 'str'): Nome do novo dono da reserva
                dono (:obj: 'str') Nome do dono da reserva
                sala (:obj: 'int') Número da sala da reserva
                data (:obj: 'str') Data da reserva
                horario (:obj: 'str') Horário da reserva

            Returns:
                True caso a alteração seja efetuada, False caso contrário
        """
        self.cursor.execute("""UPDATE RESERVAS SET dono = ? WHERE dono = ? AND sala = ?
                                AND data = ? AND horario = ?""",
                            (novo_dono, dono, sala, data, horario))
        self.salvar_alteracoes()
        if len(self.cursor.execute("""SELECT * FROM RESERVAS WHERE dono = ? AND sala = ?
                                            AND data = ? AND horario = ?""",
                                   (novo_dono, sala, data, horario)).fetchall()) == 1:
            return True
        return False

    def alterar_horario(self, novo_horario, dono, sala, data, horario):
        """ Altera o horário da reserva (caso exista)

            Args:
                novo_horario (:obj: 'str'): Novo horário da reserva
                dono (:obj: 'str') Nome do dono da reserva
                sala (:obj: 'int') Número da sala da reserva
                data (:obj: 'str') Data da reserva
                horario (:obj: 'str') Horário da reserva

            Returns:
                True caso a alteração seja efetuada, False caso contrário
        """
        self.cursor.execute("""UPDATE RESERVAS SET horario = ? WHERE dono = ? AND sala = ?
                                   AND data = ? AND horario = ?""",
                            (novo_horario, dono, sala, data, horario))

        self.salvar_alteracoes()
        result = self.cursor.execute("""SELECT * FROM RESERVAS WHERE dono = ? AND sala = ?
                                                AND data = ? AND horario = ?""",
                                     (dono, sala, data, novo_horario)).fetchall()
        if len(result) == 0:
            return True
        return False

    def remover_reserva(self, dono, sala, data, horario):
        """ Remove uma reserva dos registros

            Args:
                dono (:obj: 'str') Nome do dono da reserva
                sala (:obj: 'int') Número da sala da reserva
                data (:obj: 'str') Data da reserva
                horario (:obj: 'str') Horário da reserva

            Returns:
                 True caso a remoção da reserva for efetuada, False caso contrário
        """
        self.cursor.execute("""DELETE FROM RESERVAS WHERE dono = ? AND sala = ? AND data = ?
                                       and horario = ?""",
                            (dono, sala, data, horario))
        self.salvar_alteracoes()
        resultado = self.cursor.execute("""SELECT * FROM RESERVAS WHERE dono = ? AND sala = ?
                                                   AND data = ? AND horario = ?""",
                                        (dono, sala, data, horario)).fetchall()
        if len(resultado) == 0:
            return True
        return False

    def mostrar_reservas(self):
        """ Consulta todas as reservas efetuadas e as retorna numa lista (caso houver)

            Returns:
                reservas (:obj: 'list') of type 'tuple': Lista com reservas existentes (em tuplas)
        """
        reservas = self.cursor.execute("""SELECT * FROM RESERVAS """).fetchall()
        return reservas

    def salvar_alteracoes(self):
        """ Salva as alterações no banco de dados """
        self.conn.commit()

    def fechar(self):
        """ Fecha a conexão com o banco de dados """
        self.conn.close()
