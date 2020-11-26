class Gerenciador:
	""" Classe driver do projeto. Possui os métodos que realizam as ações principais do programa.
		Attributes:
			__socios (:obj: 'list' of :obj: 'Socio'): Lista que armazena os socios registrados.
			__reservas (:obj: 'list' of :obj: 'Reserva'): Lista que armazena as reservas efetuadas.
	"""

	def __init__(self, model_socio, model_reserva, view):
		""" Args:
				model_socio (:obj: 'Socio'): classe utilizada pelo gerenciador para criar/alterar sócios.
				model_reserva (:obj: 'Reserva'): classe utilizada pelo gerenciador para criar/alterar reservas.
				view: classe utilizada para mostrar mensagens no console.

		"""
		self.model_socio = model_socio
		self.model_reserva = model_reserva
		self.view = view
		self.__socios = []
		self.__reservas = []

	def registrar_socio(self):
		""" Cria e adiciona o socio à lista de sócios caso o mesmo não esteja registrado
			e atributos válidos forem atribuídos.

			Returns:
				True se o usuário for registrado, False caso contrário.

		"""

		socio = self.model_socio
		self.view.msg_registro_socio()
		socio.nome = input("Nome: ").title()
		socio.cargo = input("Cargo: ")
		socio.ramal = input("Ramal: ")
		if socio.validar_atributos():
			for socio in self.__socios:
				if socio.nome == socio.nome:
					self.view.msg_socio_existe(socio.nome)
					return False
			self.__socios.append(socio)
			self.view.msg_socio_registrado(socio.nome)
			return True
		else:
			self.view.msg_preencher_campos()
			self.registrar_socio()

	def criar_reserva(self):
		""" Cria e adiciona a reserva à lista de reservas caso não exista nenhuma reserva efetuada
			pelo sócio e caso a sala esteja disponível para o dia e hora específicados.

			Returns:
				True se a reserva for efetuada com, False caso contrário.

		"""
		reserva = self.model_reserva
		self.view.msg_agendar_reserva()
		reserva.socio = input("Nome do sócio: ")
		reserva.sala = input("Número da sala: ")
		reserva.data = input("Data (dd/mm/aaaa): ")
		reserva.horario = input("Horário (hh:mm): ")
		if reserva.validar_atributos():
			if self.checar_disponibilidade(reserva.socio, reserva.sala,
										   reserva.data, reserva.horario):
				self.__reservas.append(reserva)
				self.view.msg_reserva_criada(reserva)
				return True
			else:
				self.view.msg_falha_reserva()
				return False
		else:
			self.view.msg_preencher_campos()
			self.criar_reserva()

	def checar_disponibilidade(self, socio, sala, data, horario):
		""" Valida se o sócio pode realizar a reserva da sala na data e hora.

			Returns:
				True se a reserva estiver disponível, False caso contrário.

		"""
		if len(self.__reservas) >= 1:
			nomes_socios = [pessoa.nome for pessoa in self.__socios]
			socios_com_reserva = [pessoa.socio for pessoa in self.__reservas]
			for reserva in self.__reservas:
				if socio in socios_com_reserva or (reserva.data == data and reserva.horario == horario):
					return False
			if socio in nomes_socios:
				return True
		else:
			nomes_socios = [pessoa.nome for pessoa in self.__socios]
			return True if socio in nomes_socios else False

	def menu(self):
		""" Mostra um menu de opções a serem escolhidas pelo usuário.

			Returns:
				funcao (:obj: 'int'): O número equivalente à opção escolhida.

		"""
		funcao = int(input("""[===== Gerenciamento de Salas  - Morais Coworking =====]\n
							  \r[1] Registrar sócio
							  \r[2] Realizar reserva
							  \r[0] Sair\n
							  \r-->  """))
		return funcao

