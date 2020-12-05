from app.models.pessoa import Pessoa


class Socio(Pessoa):
	""" Classe que representa o sócio. Utilizada no cadastro de sócios e realização de reservas.

		Attributes:
			nome (str): Nome do sócio.
			cargo (str): Cargo ocupado pelo sócio.
			ramal (str): Ramal utilizado pelo sócio.

	"""

	def __init__(self, nome="", idade="", sexo="", cargo="", ramal="", setor=""):
		super().__init__(nome, idade, sexo)
		self.__cargo = cargo
		self.__ramal = ramal
		self.__setor = setor

	def __str__(self):
		""" :obj: 'str' Retorna a representação do objeto em string. """
		return f"Sócio: {self.nome}"

	@property
	def cargo(self):
		""" :obj: 'str': Retorna ou altera o nome do sócio. """
		return self.__cargo

	@cargo.setter
	def cargo(self, novo_cargo):
		self.__cargo = novo_cargo

	@property
	def setor(self):
		""" :obj: 'str': Retorna ou altera o cargo do sócio."""
		return self.__setor

	@setor.setter
	def setor(self, novo_setor):
		self.__setor = novo_setor

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
		if self.nome != "" and self.idade != "" and self.sexo != "" and self.__cargo != "" and self.__ramal != "" and self.__setor != "":
			return True
		return False
