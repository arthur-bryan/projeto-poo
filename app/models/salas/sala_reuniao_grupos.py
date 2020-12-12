"""
	ESTE ARQUIVO É UM MÓDULO PERTENCENTE AO PROJETO 'projeto-poo',
	DISPONÍVEL EM 'https://github.com/arthurbryan/projeto-poo'
"""

from app.models.salas.sala import Sala


class SalaReuniaoGrupos(Sala):
    """ Classe que representa uma sala de reunião por grupos. Apenas pessoas pertencentes ao
        cargo definido na sala poderão reservar esta sala.

        Attributes:
            __cargo_grupo (str): cargo permitido a realizar reservas na sala

    """

    def __init__(self, numero, vagas, cargo_grupo):
        """ Args:
            cargo_grupo (:obj: 'str'): cargo permitido a realizar reservas na sala
        """
        super().__init__(numero, vagas)
        self.__cargo_grupo = cargo_grupo

    def add_reserva(self, nova_reserva):
        """ Adiciona a reserva para a sala caso o cargo do  responsavel esteja de acordo
            com o cargo permitido na sala e caso ainda exista vaga disponível

            Args:
                nova_reserva (:obj: 'Reserva'): objeto Reserva a ser adicionado para a sala

            Returns:
                True se a reserva for registrada, False caso contrário
        """
        for reserva_existente in self.reservas:
            if (reserva_existente.data == nova_reserva.data
                    and reserva_existente.horario == nova_reserva.horario):
                return False
            if (reserva_existente.dono.nome == nova_reserva.dono.nome
                    and reserva_existente.data == nova_reserva.data
                    and reserva_existente.horario == nova_reserva.horario):
                return False
        if len(self.reservas) < self.vagas:
            if self.validar_grupo(nova_reserva):
                self.reservas.append(nova_reserva)
                return True
        return False

    def validar_grupo(self, reserva):
        """ Args:
                reserva (:obj: 'Reserva'): objeto da classe reserva a ser validado

            Returns:
                True caso o cargo do dono da reserva corresponda ao da sala, False caso contrário
        """
        if reserva.dono.cargo.upper() == self.__cargo_grupo:
            return True
        return False
