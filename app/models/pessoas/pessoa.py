from abc import ABC, abstractmethod


class Pessoa(ABC):
	""" Classe que representa uma pessoa

		Attributes:
			__nome (str): nome da pessoa
			__idade (int): idade da pessoa
			__sexo (str): sexo da pessoa

	"""

	def __init__(self, nome, idade, sexo):
		""" Args:
				nome (:obj: 'str'): nome da pessoa
				idade (:obj: 'int'): idade da pessoa
				sexo (:obj: 'str'): sexo da pessoa

		"""
		self.__nome = nome
		self.__idade = idade
		self.__sexo = sexo

	@abstractmethod
	def __str__(self):
		pass

	@property
	def nome(self):
		""" :obj: 'str': Retorna ou altera o nome do funcionário. """
		return self.__nome

	@nome.setter
	def nome(self, novo_nome):
		self.__nome = novo_nome.strip()

	@property
	def idade(self):
		""" :obj: 'int': Retorna ou altera a idade do funcionário. """
		return self.__idade

	@idade.setter
	def idade(self, nova_idade):
		self.__idade = int(nova_idade)

	@property
	def sexo(self):
		""" :obj: 'str': Retorna ou altera o sexo do funcionário. """
		return self.__sexo

	@sexo.setter
	def sexo(self, novo_sexo):
		self.__sexo = novo_sexo.strip()

	@abstractmethod
	def validar_atributos(self):
		pass
