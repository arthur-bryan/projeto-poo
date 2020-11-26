# Código driver do projeto

from socio import Socio
from reserva import Reserva
from time import sleep


class Gerenciador:

	def __init__(self):
		self.__socios = []
		self.__reservas = []

	def registrar_socio(self):
		nome = input("Nome: ").title()
		cargo = input("Cargo: ")
		ramal = input("Ramal: ")
		socio = Socio(nome, cargo, ramal)
		for socio in self.__socios:
			if socio.nome == nome:
				print("\n[!] Sócio já foi registrado!\n")
			return False
		if nome != "" and cargo != "" and ramal != "":
			self.__socios.append(socio)
			print("\n[+] Registrado!\n")
		else:
			print("\n[!] Por favor, preencha todos os campos!\n")
			self.registrar_socio()

	def criar_reserva(self, socio):
		sala = input("Número da sala: ")
		data = input("Data (dd/mm/aaaa): ")
		horario = input("Horário (hh:mm): ")
		reserva = Reserva(socio, sala, data, horario)
		if self.checar_disponibilidade(socio, sala, data, horario):
			self.__reservas.append(reserva)
			print("\n[+] Reserva realizada com sucesso!\n")
		else:
			print("\n[!] Incapaz de realizar esta reserva!\n")

	def checar_disponibilidade(self, socio, sala, data, horario):
		if len(self.__reservas) >= 1:
			nomes_socios = [pessoa.nome for pessoa in self.__socios]
			socios_com_reserva = [pessoa.nome for pessoa in self.__reservas]
			for reserva in self.__reservas:
				if socio in socios_com_reserva or (reserva.data == data and reserva.horario == horario):
					return False
			if socio in nomes_socios:
				return True
		else:
			nomes_socios = [pessoa.nome for pessoa in self.__socios]
			return True if socio in nomes_socios else False

	def menu(self):
		funcao = int(input("""[++++ Gerenciamento de Salas ++++]\n
							  \r[1] Registrar sócio
							  \r[2] Realizar reserva
							  \r[0] Sair
							  \r-->  """))
		return funcao

def main():
	gerenciador = Gerenciador()
	while True:
		try:
			funcao = gerenciador.menu()
		except ValueError:
			print("\n[!] Opção inválida!\n")
			sleep(1)
		else:
			if funcao == 1:
				gerenciador.registrar_socio()
			elif funcao == 2:
				socio = input("Nome do sócio: ").title()
				gerenciador.criar_reserva(socio)
			elif funcao == 0:
				print("\n[-] Saindo...")
				sleep(1)
				exit(0)
			else:
				print("\n[!] Opção inválida!\n")
				sleep(1)

if __name__ == '__main__':
	main()

