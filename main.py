from app.models.socio import Socio
from app.models.reserva import Reserva
from app.views.view import View
from app.controllers.gerenciador import Gerenciador
from time import sleep

def main():
    gerenciador = Gerenciador(Socio, Reserva, View)
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
                gerenciador.criar_reserva()
            elif funcao == 3:
                gerenciador.show_users()
            elif funcao == 4:
                gerenciador.show_reservas()
            elif funcao == 0:
                print("\n[-] Saindo...")
                sleep(1)
                exit(0)
            else:
                print("\n[!] Opção inválida!\n")
                sleep(1)

if __name__ == '__main__':
    main()


