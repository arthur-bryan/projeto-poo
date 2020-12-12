"""
    ESTE ARQUIVO É UM MÓDULO PERTENCENTE AO PROJETO 'projeto-poo',
    DISPONÍVEL EM 'https://github.com/arthurbryan/projeto-poo'
"""


class Sala:
    """ Classe que representa a sala de reunião. Utilizada no ato da reserva pelos sócios

        Attributes:
            __numero (int): número da sala
            __vagas (int): quantidade de vagas da sala
            __reservas (list): lista de reservas realizadas para esta sala

    """

    def __init__(self, numero, vagas):
        """ Args:
                numero (:obj: 'int'): o número da sala
                vagas (:obj: 'int'): quantidade de vagas da sala

        """
        self.__numero = numero
        self.__vagas = vagas
        self.__reservas = []

    def __str__(self):
        return f"Sala: {self.__numero}"

    def add_reserva(self, nova_reserva):
        """ Adiciona a reserva para a sala caso ainda exista vaga disponível

            Args:
                nova_reserva (:obj: 'Reserva'): objeto Reserva a ser adicionado para a sala

            Returns:
                True se a reserva for registrada, False caso contrário

        """
        for reserva_existente in self.__reservas:
            if (reserva_existente.data == nova_reserva.data and
                    reserva_existente.horario == nova_reserva.horario):
                return False
            if (reserva_existente.dono.nome == nova_reserva.dono.nome
                    and reserva_existente.data == nova_reserva.data
                    and reserva_existente.horario == nova_reserva.horario):
                return False
        if len(self.__reservas) < self.__vagas:
            self.__reservas.append(nova_reserva)
            return True
        return False

    @property
    def numero(self):
        """ :obj: 'int': Retorna ou altera o número da sala """
        return self.__numero

    @numero.setter
    def numero(self, novo_numero):
        self.__numero = int(novo_numero)

    @property
    def vagas(self):
        """ :obj: 'int': Retorna a quantidade de vagas na sala """
        return self.__vagas

    @property
    def reservas(self):
        """ :obj: 'list' of :obj: 'Reserva': Retorna uma lista com as reservas realizadas para
            esta sala """
        return self.__reservas
