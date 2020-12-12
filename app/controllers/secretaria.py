from app.database import Conexao
from datetime import datetime
import os


class Secretaria:
    """ Classe driver do projeto. Possui os métodos que realizam as ações principais do programa.
        Attributes:
            model_funcionario (Funcionario): classe utilizada para representar funcionarios
            model_socio (Socio): classe utilizada pelo gerenciador para criar/alterar sócios
            model_sala_grupo (SalaReuniaoGrupos): classe que representa as salas de reuniões por grupo
            model_sala_auditorio (Auditorio): classe que representa os auditórios
            view (View): classe Reserva utilizada para exibições no console
            __funcionarios (list): lista que armazena os socios registrados
            __socios (list): lista que armazena os socios registrados
            sala1-4 (Sala): objetos do tipo Sala com seus respectivos numeros e vagas
            __salas (tuple): tupla que armazena as salas da empresa

    """

    def __init__(self, model_funcionario, model_socio, model_sala_grupo, model_sala_auditorio, model_reserva, view):
        """ Args:
                model_funcionario (:class: 'Funcionario'): classe utilizada para representar funcionarios
                model_socio (:class: 'Socio'): classe utilizada pelo gerenciador para criar/alterar sócios
                model_sala_grupo (:class: 'SalaReuniaoGrupos'): classe que representa as salas de reuniões por grupo
                model_sala_auditorio (:class: 'Auditorio'): classe que representa os auditórios
                model_reserva (:class: 'Reserva'): classe utilizada pelo gerenciador para criar/alterar reservas
                view (:class: 'View'): classe utilizada para mostrar mensagens no console

        """
        diretorio_atual = os.path.join(os.getcwd(), 'app/database.db')
        self.conexao = Conexao(diretorio_atual)
        self.model_funcionario = model_funcionario
        self.model_socio = model_socio
        self.model_reserva = model_reserva
        self.view = view
        self.__socios = []
        self.__funcionarios = []
        sala1 = model_sala_auditorio(numero=1, vagas=50)
        sala2 = model_sala_grupo(numero=2, vagas=55, cargo_grupo="CTO")
        sala3 = model_sala_auditorio(numero=3, vagas=60)
        sala4 = model_sala_grupo(numero=4, vagas=70, cargo_grupo="CFO")
        self.__salas = (sala1, sala2, sala3, sala4)

    def registrar_funcionario(self):
        """ Cria e adiciona o funcionario à lista de sócios caso o mesmo não esteja registrado
            e atributos válidos forem atribuídos.

            Returns:
                True se o usuário for registrado, False caso contrário.

        """

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
                    self.view.msg_funcionario_existe(funcionario.nome)
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
        """ Cria e adiciona a reserva à lista de reservas caso a sala esteja disponível para o dia e hora
            específicados """
        self.view.msg_agendar_reserva()
        reserva = self.model_reserva()
        reserva.dono = input("Nome do responsável pela reserva: ").title().strip()
        if self.esta_registrado(reserva.dono):
            reserva.dono = self.objeto_por_nome(reserva.dono)
            reserva.sala = int(input("Número da sala: ").strip())
            reserva.data = input("Data (dd/mm/aaaa): ".strip())
            try:
                datetime.strptime(reserva.data, '%d/%m/%Y')
                reserva.horario = input("Horário (hh:mm): ".strip())
                datetime.strptime(reserva.horario, '%H:%M')
            except ValueError:
                print("\n[ ! ] Formato inválido!\n")
                self.criar_reserva()
            else:
                if reserva.validar_atributos():
                    reserva.sala = self.validar_numero_sala(reserva.sala)
                    if reserva.sala is not None:
                        self.conexao.inserir_reserva(reserva)
                        reserva.sala.add_reserva(reserva)
                        self.view.msg_reserva_criada(reserva)
                        return
                    else:
                        self.view.msg_falha_reserva()
                else:
                    self.view.msg_preencher_campos()
        else:
            self.view.msg_nao_registrado(reserva.dono)

    def esta_registrado(self, pessoa):
        """ Busca ocorrência de um nome nos atributos dos objetos Socios e Funcionarios já registrados

            Args:
                pessoa (:obj: 'str'): nome a ser consultado

            Returns:
                True caso o nome seja encontrado, False caso contrário
        """
        socios_registrados = [socio.nome for socio in self.__socios]
        funcionarios_registrados = [funcionario.nome for funcionario in self.__funcionarios]
        if pessoa in socios_registrados or pessoa in funcionarios_registrados:
            return True
        return False

    def objeto_por_nome(self, nome):
        """ Retorna o objeto baseado em seu atributo 'nome' se ele estiver nas listas de socios ou funcionarios

            Args:
                nome (:obj: 'str') Nome a ser buscado entre os atributos dos objetos

            Returns:
                objeto (:obj: 'Socio') caso o nome seja encontrado como atributo nome de um objeto do tipo Socio ou
                (:obj: 'Funcionario') caso seja encontrado como atributo de um objeto do tipo Funcionario

        """
        socios_registrados = [socio.nome for socio in self.__socios]
        funcionarios_registrados = [funcionario.nome for funcionario in self.__funcionarios]
        if nome in socios_registrados:
            objeto = self.__socios[socios_registrados.index(nome)]
        else:
            objeto = self.__funcionarios[funcionarios_registrados.index(nome)]
        return objeto

    def validar_numero_sala(self, numero):
        """ Args:
                numero (:obj: 'int'): numero a ser validado
            Returns:
                :obj: 'Sala' se o número for um numero valido de sala (entre 1 e 4), None caso contrário
        """
        for sala in self.__salas:
            if numero == sala.numero:
                return sala
        return None

    def consulta_reserva_no_dia(self):
        """ Verifica se a pessoa possui reserva na data informada """
        pessoa = input("Nome do dono: ").title().strip()
        data = input("Data a ser consultada: ")
        try:
            datetime.strptime(data, '%d/%m/%Y')
        except ValueError:
            print("[ ! ] Formato inválido!")
        else:
            reservas = self.conexao.consultar_reserva(pessoa, data)
            if reservas:
                for reserva in reservas:
                    print(f"Reserva para o dia {reserva[3]} às {reserva[4]}h na sala {reserva[2]}" +
                          f" realizada por {reserva[1]}.")

    def alterar_dono_reserva(self):
        nome = input("Nome do dono atual da reserva: ").strip().title()
        sala = int(input("Número da sala reservada: "))
        data = input("Data da reserva: ")
        try:
            datetime.strptime(data, '%d/%m/%Y')
            horario = input("Horário da reserva: ")
            datetime.strptime(horario, '%H:%M')
            novo_dono = input("Nome do novo dono da reserva: ")
        except ValueError:
            print("[ ! ] Formato inválido!")
            self.alterar_dono_reserva()
        else:
            if self.conexao.alterar_nome(novo_dono, nome, sala, data, horario):
                print("\nAlterado com sucesso!")
            else:
                print("\nIncapaz de alterar!")

    def alterar_horario_reserva(self):
        nome = input("Nome do dono da reserva: ").strip().title()
        sala = int(input("Número da sala reservada: "))
        data = input("Data da reserva: ")
        try:
            datetime.strptime(data, '%d/%m/%Y')
            horario = input("Horário atual da reserva: ")
            datetime.strptime(horario, '%H:%M')
            novo_horario = input("Novo horário da reserva: ")
            datetime.strptime(novo_horario, '%H:%M')
        except ValueError:
            print("[ ! ] Formato inválido!")
            self.alterar_horario_reserva()
        else:
            if self.conexao.alterar_horario(novo_horario, nome, sala, data, horario):
                print("\nAlterado com sucesso!")
            else:
                print("\nIncapaz de alterar!")

    def remover_reserva(self):
        nome = input("Nome do dono da reserva: ").strip().title()
        sala = int(input("Número da sala reservada: "))
        data = input("Data da reserva: ")
        try:
            datetime.strptime(data, '%d/%m/%Y')
            horario = input("Horário atual da reserva: ")
            datetime.strptime(horario, '%H:%M')
        except ValueError:
            print("[ ! ] Formato inválido!")
            self.alterar_horario_reserva()
        else:
            self.conexao.remover_reserva(nome, sala, data, horario)

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
                                  \r[4] Consultar reserva no dia
                                  \r[5] Alterar dono da reserva
                                  \r[6] Alterar hora da reserva
                                  \r[7] Mostrar sócios
                                  \r[8] Mostrar funcionários
                                  \r[9] Mostrar reservas
                                  \r[10] Remover reserva
                                  \r[11] Sair\n
                                  \r-->  """))
        return funcao
