class Reserva:
	""" Classe que representa as reservas. Utilizada na realização de reservas pelos sócios.

		Attributes:
			__socio (:obj: 'Socio'): objeto Socio responsável pela reserva
			__sala (:obj: 'Sala'): objeto Sala que receberá a reserva
			__data (str): data da reserva
			__horario (str): horário da reserva

	"""

	def __init__(self, dono="", sala="", data="", horario=""):
		""" Args:
				socio (:obj: 'Socio'): objeto Socio, dono da reserva
				sala (:obj: 'Sala'): objeto Sala que irá receber a reserva
				data (str): data da reserva
				horario (str): horário da reserva

		"""
		self.__dono = dono
		self.__sala = sala
		self.__data = data
		self.__horario = horario

	def __str__(self):
		return f"Reserva da sala {self.__sala} efetuada por {self.__dono} para o dia {self.__data} às {self.__horario}h"

	@property
	def dono(self):
		""" :obj: 'str': Retorna ou altera o nome do sócio responsável pela reserva. """
		return self.__dono

	@dono.setter
	def dono(self, novo_dono):
		self.__dono = novo_dono

	@property
	def sala(self):
		""" :obj: 'str': Retorna ou altera o número da sala reservada. """
		return self.__sala

	@sala.setter
	def sala(self, nova_sala):
		self.__sala = nova_sala

	@property
	def data(self):
		""" :obj: 'str': Retorna ou altera a data da reserva. """
		return self.__data

	@data.setter
	def data(self, nova_data):
		self.__data = nova_data

	@property
	def horario(self):
		""" :obj: 'str': Retorna ou altera o horário da reserva. """
		return self.__horario

	@horario.setter
	def horario(self, novo_horario):
		self.__horario = novo_horario

	def validar_atributos(self):
		if self.__dono != "" and self.__sala != "" and self.__data != "" and self.__horario != "":
			return True
		return False
