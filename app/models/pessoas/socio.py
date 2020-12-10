from app.models.pessoas.pessoa import Pessoa


class Socio(Pessoa):
    """ Classe que representa o sócio. Utilizada no cadastro de sócios e realização de reservas.

        Attributes:
            __cargo (str): Cargo ocupado pelo sócio.
            __ramal (str): Ramal utilizado pelo sócio.
            __setor (str): Setor do qual o sócio participa.

    """

    def __init__(self, nome="", idade="", sexo="", cargo="", ramal="", setor=""):
        """ Args:
                cargo (:obj: 'str'): Cargo ocupado pelo sócio.
                ramal (:obj: 'str'): Ramal utilizado pelo sócio.
                setor (:obj: 'str'): Setor do qual o sócio participa.

        """
        super().__init__(nome, idade, sexo)
        self.__cargo = cargo
        self.__ramal = ramal
        self.__setor = setor

    def __str__(self):
        """ :obj: 'str' Retorna a representação do objeto em string. """
        return f"Sócio: {self.nome}"

    @property
    def cargo(self):
        """ :obj: 'str': Retorna ou altera o cargo do sócio. """
        return self.__cargo

    @cargo.setter
    def cargo(self, novo_cargo):
        self.__cargo = novo_cargo.strip()

    @property
    def setor(self):
        """ :obj: 'str': Retorna ou altera o setor do sócio."""
        return self.__setor

    @setor.setter
    def setor(self, novo_setor):
        self.__setor = novo_setor.strip()

    @property
    def ramal(self):
        """ :obj: 'str': Retorna ou altera o ramal do sócio."""
        return self.__ramal

    @ramal.setter
    def ramal(self, novo_ramal):
        self.__ramal = novo_ramal.strip()

    def validar_atributos(self):
        """ Valida se os campos dos atributos foram preenchidos.

            Returns:
                True se os campos foram preenchidos, False caso contrário.

        """
        if (self.nome == "" or self.idade == "" or self.sexo == "" or self.__cargo == "" or self.__setor == ""
                or self.__ramal == ""):
            return False
        return True
