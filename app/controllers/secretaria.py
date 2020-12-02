class Secretaria:
	""" Classe driver do projeto. Possui os métodos que realizam as ações principais do programa.
		Attributes:
			model_socio (:class: 'Socio'): classe da view utilizada para gerência de socios
			model_socio (:class: 'Reserva'): classe Socio utilizada para gerência de reservas
			model_reserva (:class: 'View'): classe Reserva utilizada para exibições no console
			__socios (:obj: 'list' of :obj: 'Socio'): lista que armazena os socios registrados
			sala1-4 (:obj: 'Sala'): objetos do tipo Sala com seus respectivos numeros e vagas
			__salas (:obj: 'list' of :obj: 'Salas'): lista que armazena as salas 

	"""

	def __init__(self, model_socio, model_sala, model_reserva, view):
		""" Args:
				model_socio (:class: 'Socio'): classe utilizada pelo gerenciador para criar/alterar sócios
				model_sala (:class: 'Sala'): classe utilizada pelo gerenciador para criar as salas
				model_reserva (:class: 'Reserva'): classe utilizada pelo gerenciador para criar/alterar reservas
				view (:class: 'View'): classe utilizada para mostrar mensagens no console

		"""
		self.model_socio = model_socio
		self.model_reserva = model_reserva
		self.view = view
		self.__socios = []
		sala1 = model_sala(numero=1, vagas=50)
		sala2 = model_sala(numero=2, vagas=55)
		sala3 = model_sala(numero=3, vagas=60)
		sala4 = model_sala(numero=4, vagas=70)
		self.__salas = (sala1, sala2, sala3, sala4)



	def registrar_socio(self):
		""" Cria e adiciona o socio à lista de sócios caso o mesmo não esteja registrado
			e atributos válidos forem atribuídos.

			Returns:
				True se o usuário for registrado, False caso contrário.

		"""

		self.view.msg_registro_socio()
		socio = self.model_socio()
		socio.nome = input("Nome: ").title().strip()
		socio.cargo = input("Cargo: ")
		socio.ramal = input("Ramal: ")
		if socio.validar_atributos():
			for pessoa in self.__socios:
				if pessoa.nome == socio.nome:
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
		socios_com_reserva = [socio.nome for socio in self.__socios]
		self.view.msg_agendar_reserva()
		reserva = self.model_reserva()
		reserva.socio = input("Nome do sócio: ").title().strip()
		reserva.sala = int(input("Número da sala: "))
		reserva.data = input("Data (dd/mm/aaaa): ")
		reserva.horario = input("Horário (hh:mm): ")
		if reserva.validar_atributos():
			for sala in self.__salas:
				if sala.numero == reserva.sala and reserva.socio in socios_com_reserva:
					sala.add_reserva(reserva)
					self.view.msg_reserva_criada(reserva)
					return True
			self.view.msg_falha_reserva()
		else:
			self.view.msg_preencher_campos()
			self.criar_reserva()


	def mostrar_socios(self):
		[print(user) for user in self.__socios]

	def mostrar_reservas(self):
		for sala in self.__salas:
			for reserva in sala.reservas:
				print(reserva)


	def menu(self):
		""" Mostra um menu de opções a serem escolhidas pelo usuário.

			Returns:
				funcao (:obj: 'int'): O número equivalente à opção escolhida.

		"""
		funcao = int(input("""[===== Gerenciamento de Salas  - Morais Coworking =====]\n
							  \r[1] Registrar sócio
							  \r[2] Realizar reserva
							  \r[3] Mostrar sócios
							  \r[4] Mostrar reservas
							  \r[0] Sair\n
							  \r-->  """))
		return funcao

