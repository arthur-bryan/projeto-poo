from app.models.sala import Sala


class SalaReuniaoGrupos(Sala):

    def __init__(self, numero, vagas, cargo_grupo):
        super().__init__(numero, vagas)
        self.__cargo_grupo = cargo_grupo

    def add_reserva(self, nova_reserva):
        """ Adiciona a reserva para a sala caso ainda exista vaga disponível

            Args:
                nova_reserva (:obj: 'Reserva'): objeto Reserva a ser adicionado para a sala

            Returns:
                True se a reserva for registrada, False caso contrário

        """
        for reserva_existente in self.reservas:
            if reserva_existente.data == nova_reserva.data and reserva_existente.horario == nova_reserva.horario:
                return False
            if reserva_existente.socio.nome == nova_reserva.socio.nome:
                return False
        if len(self.reservas) < self.vagas:
            if self.validar_grupo(nova_reserva):
                self.reservas.append(nova_reserva)
                return True
        return False

    def validar_grupo(self, reserva):
        return True if reserva.dono.cargo == self.__cargo_grupo else False
