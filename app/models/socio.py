class Socio:
	""" Classe que representa o sócio. Utilizada no cadastro de sócios e realização de reservas.

		Attributes:
			__nome (str): Nome do sócio.
			__cargo (str): Cargo ocupado pelo sócio.
			__ramal (str): Ramal utilizado pelo sócio.

	"""
	def __init__(self, nome="", cargo="", ramal=""):
		self.__nome = nome
		self.__cargo = cargo
		self.__ramal = ramal

	def __str__(self):
		""" :obj: 'str' Retorna a representação do objeto em string. """
		return f"{self.__nome}"

	@property
	def nome(self):
		""" :obj: 'str': Retorna ou altera o nome do sócio. """
		return self.__nome

	@nome.setter
	def nome(self, novo_nome):
		self.__nome = novo_nome

	@property
	def cargo(self):
		""" :obj: 'str': Retorna ou altera o cargo do sócio."""
		return self.__cargo

	@cargo.setter
	def cargo(self, novo_cargo):
		self.__cargo = novo_cargo

	@property
	def ramal(self):
		""" :obj: 'str': Retorna ou altera o ramal do sócio."""
		return self.__ramal

	@ramal.setter
	def ramal(self, novo_ramal):
		self.__ramal = novo_ramal

	def validar_atributos(self):
		""" Valida se os campos dos atributos foram preenchidos.

			Returns:
				True se os campos foram preenchidos, False caso contrário.

		"""
		if self.__nome != "" and self.__cargo != "" and self.__ramal != "":
			return True
		return False
