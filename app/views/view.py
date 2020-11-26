class View:

	@staticmethod
	def msg_registro_socio():
		print("\n[===== Registro de Sócio =====]\n")

	@staticmethod
	def msg_agendar_reserva():
		print("\n[===== Agendamento de Reserva =====]\n")

	@staticmethod
	def msg_socio_registrado(nome):
		print(f"\n[+] O sócio {nome} foi registrado com sucesso!\n")

	@staticmethod
	def msg_socio_existe(nome):
		print(f"\n[!] O sócio {nome} já está registrado!\n")

	@staticmethod
	def msg_preencher_campos():
		print("\n[!] Por favor, preencha todos os campos!\n")

	@staticmethod
	def msg_reserva_criada(reserva):
		print(f"""\n[+] Reserva efetuada com sucesso!
	  			  \r[+] Agendado para {reserva.data} às {reserva.horario}h na sala {reserva.sala}.\n""")

	@staticmethod
	def msg_falha_reserva():
		print("\n[!] Incapaz de realizar esta reserva!\n")


