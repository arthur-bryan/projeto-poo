"""
    ESTE ARQUIVO É UM MÓDULO PERTENCENTE AO PROJETO 'projeto-poo',
    DISPONÍVEL EM 'https://github.com/arthurbryan/projeto-poo'
"""

import os
import sys
from datetime import datetime
from app.models.database import Conexao

caminho_database = os.path.join(os.getcwd(), 'app', 'database', 'database.db')


class Secretaria:
    """ Classe driver do projeto. Possui os métodos que realizam as ações principais do programa.
        Attributes:
            conexao (Conexao): classe utilizada para se conectar e fazer consultas no banco de dados
            model_funcionario (Funcionario): classe utilizada para representar funcionarios
            model_socio (Socio): classe utilizada pelo gerenciador para criar/alterar sócios
            model_sala_grupo (SalaReuniaoGrupos): classe que representa salas de reuniões por grupo
            model_sala_auditorio (Auditorio): classe que representa os auditórios
            view (View): classe Reserva utilizada para exibições no console
            __funcionarios (list): lista que armazena os socios registrados
            __socios (list): lista que armazena os socios registrados
            __sala1-4 (Sala): objetos do tipo Sala com seus respectivos numeros e vagas
            __salas (tuple): tupla que armazena as salas da empresa
    """

    def __init__(self, model_funcionario, model_socio, model_sala_grupo, model_sala_auditorio,
                 model_reserva, view):
        """ Args:
                model_funcionario (:class: 'Funcionario'): Classe que representa os funcionarios
                model_socio (:class: 'Socio'): Classe que representa os sócios
                model_sala_grupo (:class: 'SalaReuniaoGrupos'): representa  salas de reunião
                model_sala_auditorio (:class: 'Auditorio'): Classe que representa os auditórios
                model_reserva (:class: 'Reserva'): Classe que representa as reservas
                view (:class: 'View'): Classe utilizada para exibir mensagens no console
        """
        try:
            self.conexao = Conexao(caminho_database)
        except Exception:
            self.sair(1)
        self.model_funcionario = model_funcionario
        self.model_socio = model_socio
        self.model_reserva = model_reserva
        self.view = view
        self.__socios = []
        self.__funcionarios = []
        self.__sala1 = model_sala_auditorio(numero=1, vagas=50)
        self.__sala2 = model_sala_grupo(numero=2, vagas=55, cargo_grupo="CTO")
        self.__sala3 = model_sala_auditorio(numero=3, vagas=60)
        self.__sala4 = model_sala_grupo(numero=4, vagas=70, cargo_grupo="CFO")
        self.__salas = (self.__sala1, self.__sala2, self.__sala3, self.__sala4)

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
        funcionario.sexo = input("Sexo: ").title().strip()
        funcionario.cargo = input("Cargo: ").title().strip()
        funcionario.numero_id = input("Número de identificação: ")
        funcionario.salario = float(input("Salário: ").strip())
        if funcionario.validar_atributos():
            for pessoa in self.__funcionarios:
                if pessoa.nome == funcionario.nome:
                    self.view.msg_funcionario_existe(funcionario.nome)
            self.__funcionarios.append(funcionario)
            self.view.msg_registrado(funcionario.nome)
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
        socio.idade = int(input("Idade: ").strip())
        socio.sexo = input("Sexo: ").title().strip()
        socio.cargo = input("Cargo: ").title().strip()
        socio.ramal = input("Ramal: ").strip()
        socio.setor = input("Setor: ").title().strip()
        if socio.validar_atributos():
            for pessoa in self.__socios:
                if pessoa.nome == socio.nome:
                    self.view.msg_socio_existe(socio.nome)
                    return False
            self.__socios.append(socio)
            self.view.msg_registrado(socio.nome)
            return True
        self.view.msg_preencher_campos()
        self.registrar_socio()
        return False

    def criar_reserva(self):
        """ Cria e adiciona a reserva à lista de reservas caso a sala esteja disponível para
            o dia e hora específicados
        """
        self.view.msg_agendar_reserva()
        reserva = self.model_reserva()
        reserva.dono = input("Nome do responsável pela reserva: ").title().strip()
        if self.esta_registrado(reserva.dono):
            reserva.dono = self.objeto_por_nome(reserva.dono)
            try:
                reserva.sala = int(input("Número da sala: ").strip())
                reserva.data = input("Data (dd/mm/aaaa): ").strip()
                datetime.strptime(reserva.data, '%d/%m/%Y')
                reserva.horario = input("Horário (hh:mm): ").strip()
                datetime.strptime(reserva.horario, '%H:%M')
            except ValueError:
                self.view.msg_formato_invalido()
                self.criar_reserva()
            else:
                if reserva.validar_atributos():
                    reserva.sala = self.validar_numero_sala(reserva.sala)
                    if reserva.sala is not None:
                        if reserva.sala.add_reserva(reserva):
                            self.conexao.inserir_reserva(reserva)
                            self.view.msg_reserva_criada(reserva)
                        else:
                            self.view.msg_falha_reserva()
                    else:
                        self.view.msg_falha_reserva()
                else:
                    self.view.msg_preencher_campos()
        else:
            self.view.msg_nao_registrado(reserva.dono)

    def esta_registrado(self, pessoa):
        """ Verifica se o sócio ou funcionário já foi registrado baseando no nome

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
        """ Retorna o objeto baseado em seu atributo 'nome' se ele estiver nas listas de
            socios ou funcionarios

            Args:
                nome (:obj: 'str') Nome a ser buscado entre os atributos dos objetos

            Returns:
                objeto (:obj: 'Socio') caso o nome seja encontrado como atributo nome de
                um objeto do tipo Socio ou (:obj: 'Funcionario') caso seja encontrado como
                atributo de um objeto do tipo Funcionario
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
                :obj: 'Sala' se o número estiver entre 1 e 4, None caso contrário
        """
        for sala in self.__salas:
            if numero == sala.numero:
                if sala.numero == 2:
                    return self.__sala2
                if sala.numero == 4:
                    return self.__sala4
                return sala
        return None

    def consulta_reserva_no_dia(self):
        """ Verifica se a pessoa possui reserva na data informada """
        pessoa = input("Nome do dono: ").title().strip()
        data = input("Data a ser consultada: ").strip()
        try:
            datetime.strptime(data, '%d/%m/%Y')
        except ValueError:
            self.view.msg_formato_invalido()
        else:
            reservas = self.conexao.consultar_reserva(pessoa, data)
            if reservas:
                self.view.mostrar_reservas(reservas)
            else:
                self.view.msg_nao_tem_reserva(pessoa, data)

    def alterar_dono_reserva(self):
        """ Recebe os atributos da reserva a ser alterada e o nome do novo dono, então tenta
            alterar o nome do dono dessa reserva
        """

        nome = input("Nome do dono atual da reserva: ").strip().title()
        sala = int(input("Número da sala reservada: ").strip())
        data = input("Data da reserva: ")
        try:
            datetime.strptime(data, '%d/%m/%Y')
            horario = input("Horário da reserva: ").strip()
            datetime.strptime(horario, '%H:%M')
            novo_dono = input("Nome do novo dono da reserva: ").title().strip()
        except ValueError:
            self.view.msg_formato_invalido()
            self.alterar_dono_reserva()
        else:
            try:
                novo_dono = self.objeto_por_nome(novo_dono)
            except ValueError:
                self.view.msg_nao_registrado(novo_dono)
            else:
                if self.conexao.alterar_nome(novo_dono.nome, nome, sala, data, horario):
                    self.view.msg_sucesso_alteracao()
                else:
                    self.view.msg_falha_alteracao()
                    self.alterar_dono_reserva()

    def alterar_horario_reserva(self):
        """ Recebe os atributos da reserva a ser alterada e novo horario, então tenta alterar
            o horário dessa reserva
        """

        nome = input("Nome do dono da reserva: ").strip().title()
        sala = int(input("Número da sala reservada: ").strip())
        data = input("Data da reserva: ").strip()
        try:
            datetime.strptime(data, '%d/%m/%Y')
            horario = input("Horário atual da reserva: ").strip()
            datetime.strptime(horario, '%H:%M')
            novo_horario = input("Novo horário da reserva: ").strip()
            datetime.strptime(novo_horario, '%H:%M')
        except ValueError:
            self.view.msg_formato_invalido()
            self.alterar_horario_reserva()
        else:
            if self.conexao.alterar_horario(novo_horario, nome, sala, data, horario):
                self.view.msg_sucesso_alteracao()
            else:
                self.view.msg_falha_alteracao()

    def remover_reserva(self):
        """ Remove a reserva caso encontrada no banco de dados baseado em seus atributos """
        try:
            nome = input("Nome do dono da reserva: ").strip().title()
            sala = int(input("Número da sala reservada: ").strip())
            data = input("Data da reserva: ").strip()
            datetime.strptime(data, '%d/%m/%Y')
            horario = input("Horário atual da reserva: ").strip()
            datetime.strptime(horario, '%H:%M')
        except ValueError:
            self.view.msg_formato_invalido()
            self.remover_reserva()
        else:
            resultado = self.conexao.remover_reserva(nome, sala, data, horario)
            self.view.msg_remocao(resultado)

    def mostrar_socios(self):
        """ Exibe os socios registrados """
        self.view.mostrar_socios(self.__socios)

    def mostrar_funcionarios(self):
        """ Exibe os funcionários registrados """
        self.view.mostrar_funcionarios(self.__funcionarios)

    def mostrar_reservas(self):
        """ Exibe as reservas registradas """
        self.view.mostrar_reservas(self.conexao.mostrar_reservas())

    @staticmethod
    def sair(codigo):
        """ Sai do programa com o codigo de saída informado

            Args:
                codigo (:obj: 'int'): Códio do sys.exit()
        """
        sys.exit(codigo)

    @staticmethod
    def menu():
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
