from app.models.salas.sala import Sala


class Auditorio(Sala):
	""" Classe que representa um auditório

		Attributes:
			__projetor_ligado (bool): representa o status do projetor do autitório

	"""

	def __init__(self, numero, vagas):
		super().__init__(numero, vagas)
		self.__projetor_ligado = False

	def __str__(self):
		return f"Auditório: {self.numero}"

	def ligar_projetor(self):
		""" Muda o status do projetor para True """
		self.__projetor_ligado = True

	def desligar_projetor(self):
		""" Muda o status do projetor para False """
		self.__projetor_ligado = False

	@property
	def projetor_ligado(self):
		""" :obj: 'bool': return True se o projetor estiver ligado, False caso contrário """
		return self.__projetor_ligado
