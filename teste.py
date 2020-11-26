# Código driver do projeto

from socio import Socio
from reserva import Reserva
from time import sleep

socios = []
reservas = []

def registrar_socio():
	nome = input("Nome: ").title()
	cargo = input("Cargo: ")
	ramal = input("Ramal: ")
	socio = Socio(nome, cargo, ramal)
	for socio in socios:
		if socio.nome == nome:
			print("\n[!] Sócio já foi registrado!\n")
			return False
	socios.append(socio)
	print("\n[+] Registrado!\n")


def criar_reserva(socio):
	sala = input("Número da sala: ")
	data = input("Data (dd/mm/aaaa): ")
	horario = input("Horário (hh:mm): ")
	reserva = Reserva(socio, sala, data, horario)
	if checar_disponibilidade(socio, sala, data, horario):
		reservas.append(reserva)
		print("\n[+] Reserva realizada com sucesso!\n")
	else:
		print("\n[!] Incapaz de realizar esta reserva!\n")

def checar_disponibilidade(socio, sala, data, horario):
	if len(reservas) >= 1:
		socios_com_reserva = [pessoa.nome for pessoa in reservas]
		for reserva in reservas:
			if socio in socios_com_reserva or (reserva.data == data and reserva.horario == horario):
				return False
			return True
	else:
		nomes_socios = [pessoa.nome for pessoa in socios]
		if socio not in nomes_socios:
			return False

def menu():
	funcao = int(input("""[++++ Gerenciamento de Salas ++++]\n
						  \r[1] Registrar sócio
						  \r[2] Realizar reserva
						  \r[0] Sair
						  \r-->  """))
	return funcao

def main():
	while True:
		try:
			funcao = menu()
		except ValueError:
			print("\n[!] Opção inválida!\n")
			sleep(1)
		else:
			if funcao == 1:
				registrar_socio()
			elif funcao == 2:
				socio = input("Nome do sócio: ")
				criar_reserva(socio)
			elif funcao == 0:
				print("\n[-] Saindo...")
				sleep(1)
				exit(0)
			else:
				print("\n[!] Opção inválida!\n")
				sleep(1)

if __name__ == '__main__':
	main()

