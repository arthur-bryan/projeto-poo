from app.models.sala import Sala


class Auditorio(Sala):

	def __init__(self, numero, vagas, palestrante):
		super().__init__(numero, vagas)
		self.__palestrante = palestrante
		self.__projetor = False

	def ligar_projetor(self):
		self.__projetor = True

	def desligar_projetor(self):
		self.__projetor = False

	def get_projetor_status(self):
		return "Projetor está ligado" if self.__projetor is True else "Projetor está desligado"
