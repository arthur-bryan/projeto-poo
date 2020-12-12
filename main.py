"""
__author__ = ['Renato Fernandes', 'Guilherme de Lima', 'Arthur Bryan']
__copyright__ = 'Copyright 2020, projeto-poo'
__credits__ = ['Renato Fernandes', 'Guilherme de Lima', 'Arthur Bryan']
__license__ = 'MIT License'
__version__ = '3.1.0'
__maintainer__ = ['Renato Fernandes', 'Guilherme de Lima', 'Arthur Bryan']
__email__ = ['arthurbryan2030@.@gmail.com']
__status__ = 'Production'
"""

from app.models.pessoas.funcionario import Funcionario
from app.models.pessoas.socio import Socio
from app.models.reserva import Reserva
from app.models.salas.auditorio import Auditorio
from app.models.salas.sala_reuniao_grupos import SalaReuniaoGrupos
from app.views.view import View
from app.controllers.secretaria import Secretaria


def main():
    """ Função principal que inicializa a Secretaria e realiza as ações baseado no número
        escolhido pelo usuário
    """
    secretaria = Secretaria(Funcionario, Socio, SalaReuniaoGrupos, Auditorio, Reserva, View)
    while True:
        try:
            funcao = secretaria.menu()
        except ValueError:
            secretaria.view.msg_opcao_invalida()
        else:
            if funcao == 1:
                secretaria.registrar_socio()
            elif funcao == 2:
                secretaria.registrar_funcionario()
            elif funcao == 3:
                secretaria.criar_reserva()
            elif funcao == 4:
                secretaria.consulta_reserva_no_dia()
            elif funcao == 5:
                secretaria.alterar_dono_reserva()
            elif funcao == 6:
                secretaria.alterar_horario_reserva()
            elif funcao == 7:
                secretaria.mostrar_socios()
            elif funcao == 8:
                secretaria.mostrar_funcionarios()
            elif funcao == 9:
                secretaria.mostrar_reservas()
            elif funcao == 10:
                secretaria.remover_reserva()
            elif funcao == 11:
                secretaria.conexao.fechar()
                secretaria.sair(1)
            else:
                secretaria.view.msg_formato_invalido()


if __name__ == '__main__':
    main()
