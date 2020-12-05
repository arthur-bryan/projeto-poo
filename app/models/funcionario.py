from app.models.pessoa import Pessoa


class Funcionario(Pessoa):
	""" Classe que representa o sócio. Utilizada no cadastro de sócios e realização de reservas.

		Attributes:
			__nome (str): Nome do sócio.
			__cargo (str): Cargo ocupado pelo sócio.
			__ramal (str): Ramal utilizado pelo sócio.

	"""

	def __init__(self, nome="", idade="", sexo="", cargo="", numero_id="", salario=""):
		super().__init__(nome, idade, sexo)
		self.__cargo = cargo
		self.__numero_id = numero_id
		self.__salario = salario

	def __str__(self):
		""" :obj: 'str' Retorna a representação do objeto em string. """
		return f"Funcionário: {self.nome}"

	@property
	def cargo(self):
		""" :obj: 'str': Retorna ou altera o nome do funcionário. """
		return self.__cargo

	@cargo.setter
	def cargo(self, novo_cargo):
		self.__cargo = novo_cargo

	@property
	def numero_id(self):
		""" :obj: 'str': Retorna ou altera o cargo do sócio."""
		return self.__numero_id

	@numero_id.setter
	def numero_id(self, novo_id):
		self.__numero_id = novo_id

	@property
	def salario(self):
		""" :obj: 'str': Retorna ou altera o ramal do sócio."""
		return self.__salario

	@salario.setter
	def salario(self, novo_salario):
		self.__salario = novo_salario

	def validar_atributos(self):
		""" Valida se os campos dos atributos foram preenchidos.

			Returns:
				True se os campos foram preenchidos, False caso contrário.

		"""
		if self.nome != "" and self.__cargo != "" and self.idade != "" and self.__numero_id != "" and self.__salario != "":
			return True
		return False
