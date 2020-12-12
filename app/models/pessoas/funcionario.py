"""
    ESTE ARQUIVO É UM MÓDULO PERTENCENTE AO PROJETO 'projeto-poo',
    DISPONÍVEL EM 'https://github.com/arthurbryan/projeto-poo'
"""

from app.models.pessoas.pessoa import Pessoa


class Funcionario(Pessoa):
    """ Classe que representa o funcionário. Utilizada no cadastro de pessoas e realização de
        reservas

        Attributes:
            __cargo (str): Cargo ocupado pelo funcionário
            __numero_id (str): ID do funcionário
            __salario (float): Salário do funcionário

    """

    def __init__(self, nome="", idade="", sexo="", cargo="", numero_id="", salario=""):
        """ Args:
                cargo (:obj: 'str'): Cargo ocupado pelo funcionário
                numero_id (:obj: 'str'): ID do funcionário
                salario (:obj: 'float'): Salário do funcionário
        """
        super().__init__(nome, idade, sexo)
        self.__cargo = cargo
        self.__numero_id = numero_id
        self.__salario = salario

    def __str__(self):
        """ :obj: 'str' Retorna a representação do objeto em string. """
        return f"Funcionário: {self.nome}"

    @property
    def cargo(self):
        """ :obj: 'str': Retorna ou altera o cargo do funcionário. """
        return self.__cargo

    @cargo.setter
    def cargo(self, novo_cargo):
        self.__cargo = novo_cargo.strip()

    @property
    def numero_id(self):
        """ :obj: 'str': Retorna ou altera o id do funcionário."""
        return self.__numero_id

    @numero_id.setter
    def numero_id(self, novo_id):
        self.__numero_id = novo_id.strip()

    @property
    def salario(self):
        """ :obj: 'float': Retorna ou altera o salário do funcionário."""
        return self.__salario

    @salario.setter
    def salario(self, novo_salario):
        self.__salario = float(novo_salario)

    def validar_atributos(self):
        """ Valida se os campos dos atributos foram preenchidos.

            Returns:
                True se os campos foram preenchidos, False caso contrário.

        """
        if (self.nome == "" or self.idade == "" or self.sexo == "" or self.__cargo == ""
                or self.__numero_id == "" or self.__salario == ""):
            return False
        return True
