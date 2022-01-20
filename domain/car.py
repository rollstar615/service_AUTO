from domain.entity import Entity

class Car(Entity):

    def __init__(self,id_car,model,an_cumparare,nr_km,garantie,an_fabricatie):
        super().__init__(id_car)
        self.__model=model
        self.__an_cumparare=an_cumparare
        self.__nr_km=nr_km
        self.__garantie=garantie
        self.__an_fabricatie=an_fabricatie

    @property
    def model(self):
        return self.__model

    @property
    def an_cumparare(self):
        return self.__an_cumparare

    @property
    def nr_km(self):
        return self.__nr_km

    @property
    def garantie(self):
        return self.__garantie

    @property
    def an_fabricatie(self):
        return self.__an_fabricatie

    def __str__(self):
        return 'Car {}. {}.  {}. {}. {}. {}'.format(self.id_entity,
                                                    self.model,
                                                    self.an_cumparare,
                                                    self.nr_km,
                                                    self.garantie,
                                                    self.an_fabricatie)

    def __eq__(self, other):
        if type(self)!=type(other):
            return False
        return self.id_entity ==other.id_entity
