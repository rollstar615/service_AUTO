from domain.entity import Entity


class Client(Entity):

    def __init__(self, id_client, nume, prenume, cnp, data_nasterii, data_inregistrarii):
        super().__init__(id_client)
        self.__nume = nume
        self.__prenume = prenume
        self.__cnp = cnp
        self.__data_nasterii = data_nasterii
        self.__data_inregistrarii=data_inregistrarii

    @property
    def nume(self):
        return self.__nume

    @property
    def prenume(self):
        return self.__prenume

    @property
    def cnp(self):
        return self.__cnp

    @property
    def data_nasterii(self):
        return self.__data_nasterii

    @property
    def data_inregistrarii(self):
        return self.__data_inregistrarii

    def __str__(self):
        return 'Client {}. {}. {}. {}. {}'.format(self.id_entity,
                                               self.nume,
                                               self.cnp,
                                               self.data_nasterii,
                                               self.data_inregistrarii)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.id_entity == other.id_entity
