from app.models.funcionario import Funcionario
from app.models.socio import Socio
from app.models.reserva import Reserva
from app.models.auditorio import Auditorio
from app.models.sala_reuniao_grupos import SalaReuniaoGrupos
from app.views.view import View
from app.controllers.secretaria import Secretaria
from time import sleep


def main():
    secretaria = Secretaria(Funcionario, Socio, SalaReuniaoGrupos, Auditorio, Reserva, View)
    while True:
        try:
            funcao = secretaria.menu()
        except ValueError:
            print("\n[!] Opção inválida!\n")
            sleep(1)
        else:
            if funcao == 1:
                secretaria.registrar_socio()
            elif funcao == 2:
                secretaria.registrar_funcionario()
            elif funcao == 3:
                secretaria.criar_reserva()
            elif funcao == 4:
                secretaria.mostrar_socios()
            elif funcao == 5:
                secretaria.mostrar_funcionarios()
            elif funcao == 6:
                secretaria.mostrar_reservas()
            elif funcao == 0:
                print("\n[-] Saindo...")
                sleep(1)
                exit(0)
            else:
                print("\n[!] Opção inválida!\n")
                sleep(1)


if __name__ == '__main__':
    main()


