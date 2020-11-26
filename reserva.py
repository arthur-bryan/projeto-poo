class Reserva:

	def __init__(self, socio, sala, data, horario):
		self.__nome = socio
		self.__sala = sala
		self.__data = data
		self.__horario = horario


	@property
	def nome(self):
		return self.__nome

	@property
	def sala(self):
		return self.__sala

	@property
	def data(self):
		return self.__data

	@property
	def horario(self):
		return self.__horario


