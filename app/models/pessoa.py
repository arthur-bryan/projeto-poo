class Pessoa:

	def __init__(self, nome, idade, sexo):
		self.__nome = nome
		self.__idade = idade
		self.__sexo = sexo

	def __str__(self):
		return f"Pessoa: {self.__nome}"

	@property
	def nome(self):
		return self.__nome

	@nome.setter
	def nome(self, novo_nome):
		self.__nome = novo_nome

	@property
	def idade(self):
		return self.__idade

	@idade.setter
	def idade(self, nova_idade):
		self.__idade = nova_idade

	@property
	def sexo(self):
		return self.__sexo

	@sexo.setter
	def sexo(self, novo_sexo):
		self.__sexo = novo_sexo
