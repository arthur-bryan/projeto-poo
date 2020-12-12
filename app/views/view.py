"""
    ESTE ARQUIVO É UM MÓDULO PERTENCENTE AO PROJETO 'projeto-poo',
    DISPONÍVEL EM 'https://github.com/arthurbryan/projeto-poo'
"""


class View:
    """ Classe responsável por exibir a maior parte das mensagens do programa """

    def __init__(self):
        pass

    @staticmethod
    def msg_registro_socio():
        """ Exibe um banner de registro de sócios """
        print("\n[===== Registro de Sócio =====]\n")

    @staticmethod
    def msg_registro_funcionario():
        """ Exibe um banner de registro de funcionários """
        print("\n[===== Registro de Funcionário =====]\n")

    @staticmethod
    def msg_agendar_reserva():
        """ Exibe um banner de do agendamento de reservas """
        print("\n[===== Agendamento de Reserva =====]\n")

    @staticmethod
    def msg_registrado(nome):
        """ Exibe mensafem de registro sucedido """
        print(f"\n[ + ] {nome} foi registrado com sucesso!\n")

    @staticmethod
    def msg_socio_existe(nome):
        """ Exibe uma mensagem de sócio já existente """
        print(f"\n[ ! ] O sócio {nome} já está registrado!\n")

    @staticmethod
    def msg_funcionario_existe(nome):
        """ Exibe uma mensagem de funcionário já existente """
        print(f"\n[ ! ] O funcionário {nome} já está registrado!\n")

    @staticmethod
    def msg_preencher_campos():
        """ Exibe um aviso alertando que campos não foram preenchidos """
        print("\n[ ! ] Por favor, preencha todos os campos!\n")

    @staticmethod
    def msg_reserva_criada(reserva):
        """ Exibe uma mensagem de reserva efetuada e alguns detalhes desta reserva """
        print(f"""\n[ + ] Reserva efetuada com sucesso!
	  			  \r[ + ] Agendado para {reserva.data} às {reserva.horario}h na sala {reserva.sala}.\n""")

    @staticmethod
    def msg_falha_reserva():
        """ Exibe uma mensagem para quando a reserva não puder ser efetuada """
        print("\n[ ! ] Incapaz de realizar esta reserva!\n")

    @staticmethod
    def msg_nao_registrado(nome):
        """ Exibe uma mensagem alertando que o nome informado não foi registrado  """
        print(f"\n[ ! ] {nome} não está registrado(a)!\n")

    @staticmethod
    def msg_nao_tem_reserva(pessoa, data):
        """ Exibe uma mensagem para quando a pessoa não tiver reservas no dia informado """
        print(f"\n[ + ] {pessoa} não possui reservas para o dia {data}\n")

    @staticmethod
    def mostrar_socios(socios):
        """ Exibe os sócios registrados (caso houver) """
        print("\n[===== Sócios registrados =====]\n")
        for socio in socios:
            print(socio)

    @staticmethod
    def mostrar_funcionarios(funcionarios):
        """ Exibe os funcionários registrados (caso houver) """
        print("\n[===== Funcionários registrados =====]\n")
        for funcionario in funcionarios:
            print(funcionario)

    @staticmethod
    def mostrar_reservas(reservas):
        """ Exibe as reservas registradas (caso houver) """
        print("\n[===== Reservas registradas =====]\n")
        for reserva in reservas:
            print(f"[ + ] Reserva para o dia {reserva[3]} às {reserva[4]}h na sala {reserva[2]}" +
                  f" realizada por {reserva[1]}.")

    @staticmethod
    def msg_formato_invalido():
        """ Exibe uma mensagem caso algum tipo de dado inválido seja informado """
        print("\n[ ! ] Formato inválido!\n")

    @staticmethod
    def msg_remocao(resultado_consulta):
        """ Exibe mensagem de sucesso caso a remoção seja efetuada ou uma de erro caso contrário """
        if len(resultado_consulta) == 0:
            print("\n[ + ] Removido com sucesso!\n")
        else:
            print("\n[ + ] Falha tentando remover!\n")

    @staticmethod
    def msg_sucesso_alteracao():
        """ Exibe uma mensagem de sucesso caso uma alteração no banco for efetuada """
        print("\n[ + ] Alterado com sucesso!\n")

    @staticmethod
    def msg_falha_alteracao():
        """ Exibe uma mensagem de falha caso uma alteração no banco seja mal sucedida """
        print("\n[ ! ] Falha ao tentar alterar!\n")

    @staticmethod
    def msg_falha_conexao():
        """ Exibe uma mensagem de falha caso a conexao com o banco de dados não exista """
        print("\n[ ! ] Sem conexão com o banco de dados!\n")

    @staticmethod
    def msg_opcao_invalida():
        """ Exibe uma mensagem de opção inválida """
        print("\n[ ! ] Opção inválida!\n")
