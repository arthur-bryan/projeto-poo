class Sala:
	""" Classe que representa a sala de reunião. Utilizada no ato da reserva pelos sócios.

		Attributes:
			__numero (:obj: 'int'): O número da sala.

	"""

	def __init__(self, numero)
		""" Args:
				numero (:obj: 'int'): O número da sala.

		"""
		self.__numero = numero

	def validar_numero(self):
		""" Valida o número da sala.

			Returns:
				True se o número da sala estiver entre 1 e 4, False caso contrário.

		"""
		if self.__numero >= 1 and self.__numero <= 4:
			return True
		return False


	@property
	def numero(self):
		""" :obj: 'int': Retorna ou altera o número da sala. """
		return self.__numero

	@numero.setter
	def numero(self, novo_numero):
		self.__numero = novo_numero

class Sala1(Sala):

	def __init__(self, numero):
		super().__init__(numero)
		self.__vagas = 40


class Sala2(Sala):

    def __init__(self, numero):
        super().__init__(numero)
        self.__vagas = 50


class Sala3(Sala):

    def __init__(self, numero):
        super().__init__(numero)
        self.__vagas = 55


class Sala4(Sala):

    def __init__(self, numero):
        super().__init__(numero)
        self.__vagas = 60


