class Socio:

	def __init__(self, nome, cargo, ramal):
		self.__nome = nome
		self.__cargo = cargo
		self.__ramal = ramal

	@property
	def nome(self):
		return self.__nome


	def get_nome(self):
		return self.__nome
