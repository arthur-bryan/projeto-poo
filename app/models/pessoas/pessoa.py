"""
    ESTE ARQUIVO É UM MÓDULO PERTENCENTE AO PROJETO 'projeto-poo',
    DISPONÍVEL EM 'https://github.com/arthurbryan/projeto-poo'
"""

from abc import ABC, abstractmethod


class Pessoa(ABC):
    """ Classe que representa uma pessoa

        Attributes:
            __nome (str): Nome da pessoa
            __idade (int): Idade da pessoa
            __sexo (str): Sexo da pessoa

    """

    def __init__(self, nome, idade, sexo):
        """ Args:
                nome (:obj: 'str'): Nome da pessoa
                idade (:obj: 'int'): Idade da pessoa
                sexo (:obj: 'str'): Sexo da pessoa

        """
        self.__nome = nome
        self.__idade = idade
        self.__sexo = sexo

    @abstractmethod
    def __str__(self):
        pass

    @property
    def nome(self):
        """ :obj: 'str': Retorna ou altera o nome do funcionário """
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.strip()

    @property
    def idade(self):
        """ :obj: 'int': Retorna ou altera a idade do funcionário """
        return self.__idade

    @idade.setter
    def idade(self, nova_idade):
        self.__idade = int(nova_idade)

    @property
    def sexo(self):
        """ :obj: 'str': Retorna ou altera o sexo do funcionário """
        return self.__sexo

    @sexo.setter
    def sexo(self, novo_sexo):
        self.__sexo = novo_sexo.strip()

    @abstractmethod
    def validar_atributos(self):
        """ Método abstrato obrigatório para as classes que herdam desta classe """
