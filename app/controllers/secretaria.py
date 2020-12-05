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

    def __init__(self, model_funcionario, model_socio, model_sala_grupo, model_sala_auditorio, model_reserva, view):
        """ Args:
                model_socio (:class: 'Socio'): classe utilizada pelo gerenciador para criar/alterar sócios
                model_sala (:class: 'Sala'): classe utilizada pelo gerenciador para criar as salas
                model_reserva (:class: 'Reserva'): classe utilizada pelo gerenciador para criar/alterar reservas
                view (:class: 'View'): classe utilizada para mostrar mensagens no console

        """
        self.model_funcionario = model_funcionario
        self.model_socio = model_socio
        self.model_reserva = model_reserva
        self.view = view
        self.__socios = []
        self.__funcionarios = []
        sala1 = model_sala_auditorio(numero=1, vagas=50, palestrante=None)
        sala2 = model_sala_grupo(numero=2, vagas=55, cargo_grupo="CTO")
        sala3 = model_sala_auditorio(numero=3, vagas=60, palestrante=None)
        sala4 = model_sala_grupo(numero=4, vagas=70, cargo_grupo="CFO")
        self.__salas = (sala1, sala2, sala3, sala4)

    def registrar_funcionario(self):
        self.view.msg_registro_funcionario()
        funcionario = self.model_funcionario()
        funcionario.nome = input("Nome: ").title().strip()
        funcionario.idade = int(input("Idade: "))
        funcionario.sexo = input("Sexo: ")
        funcionario.cargo = input("Cargo: ")
        funcionario.numero_id = input("Número de identificação: ")
        funcionario.salario = input("Salário: ")
        if funcionario.validar_atributos():
            for pessoa in self.__funcionarios:
                if pessoa.nome == funcionario.nome:
                    self.view.msg_socio_existe(funcionario.nome)
                    return False
            self.__funcionarios.append(funcionario)
            self.view.msg_registrado(funcionario.nome)
            return True
        else:
            self.view.msg_preencher_campos()
            self.registrar_socio()

    def registrar_socio(self):
        """ Cria e adiciona o socio à lista de sócios caso o mesmo não esteja registrado
            e atributos válidos forem atribuídos.

            Returns:
                True se o usuário for registrado, False caso contrário.

        """
        self.view.msg_registro_socio()
        socio = self.model_socio()
        socio.nome = input("Nome: ").title().strip()
        socio.idade = int(input("Idade: "))
        socio.sexo = input("Sexo: ")
        socio.cargo = input("Cargo: ")
        socio.ramal = input("Ramal: ")
        socio.setor = input("Setor: ")
        if socio.validar_atributos():
            for pessoa in self.__socios:
                if pessoa.nome == socio.nome:
                    self.view.msg_socio_existe(socio.nome)
                    return False
            self.__socios.append(socio)
            self.view.msg_registrado(socio.nome)
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
        reserva.dono = input("Nome do sócio: ").title().strip()
        for num, socio in enumerate(self.__socios):
            if reserva.dono == socio.nome:
                reserva.dono = self.__socios[num]
        reserva.sala = int(input("Número da sala: "))
        reserva.data = input("Data (dd/mm/aaaa): ")
        reserva.horario = input("Horário (hh:mm): ")
        if reserva.validar_atributos():
            for sala in self.__salas:
                if sala.numero == reserva.sala:
                    if sala.add_reserva(reserva):
                        self.view.msg_reserva_criada(reserva)
                        return True
                    else:
                        self.view.msg_falha_reserva()
        else:
            self.view.msg_preencher_campos()
            self.criar_reserva()

    def mostrar_socios(self):
        [print(user) for user in self.__socios]

    def mostrar_funcionarios(self):
        [print(user) for user in self.__funcionarios]


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
                                  \r[2] Registrar funcionário
                                  \r[3] Realizar reserva
                                  \r[4] Mostrar sócios
                                  \r[5] Mostrar funcionários
                                  \r[6] Mostrar reservas
                                  \r[0] Sair\n
                                  \r-->  """))
        return funcao
