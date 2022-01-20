from domain.entity import Entity


class Tranzactie(Entity):

    def __init__(self,id_tranzactie, id_car, id_client, suma_piese, suma_manopera, data_ora):
        super().__init__(id_tranzactie)
        self.__id_car = id_car
        self.__id_client = id_client
        self.__suma_piese = suma_piese
        self.__suma_manopera = suma_manopera
        self.__data_ora =data_ora

    @property
    def id_car(self):
        return self.__id_car

    @property
    def id_client(self):
        return self.__id_client

    @property
    def suma_piese(self):
        return self.__suma_piese

    @property
    def suma_manopera(self):
        return self.__suma_manopera

    @property
    def data_ora(self):
        return self.__data_ora

    def __str__(self):
        return '{}.Tranzactie {}.-Car {}. {}. {}. {} '.format( self.id_entity,
                                               self.id_car,
                                               self.id_client,
                                               self.suma_piese,
                                               self.suma_manopera,
                                               self. data_ora)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.id_entity == other.id_entity
