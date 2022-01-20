from domain.car import Car
from domain.tranzactie import Tranzactie
from domain.tranzactie_viewmodel import TranzactieViewModel
class TranzactieService:

    """
    Manages location logic.
    """

    def __init__(self, tranzactie_repository,car_repository, card_client_repository):
        """
        Creates a location service.
        """
        self.__tranzactie_repository = tranzactie_repository
        self.__card_client_repository=card_client_repository
        self.__car_repository=car_repository

    def add_tranzactie(self, id_tranzactie, id_car, id_client, suma_piese, suma_manopera, data_ora):
        if self.__car_repository.read(id_car) is None:
            raise ValueError('Nu exista nicio masina cu id-ul: ')
        tranzactie = Tranzactie(id_tranzactie, id_car, id_client, suma_piese, suma_manopera, data_ora)
        car = self.__car_repository.read(tranzactie.id_car)
        garantie = car.garantie
        card_client=self.__card_client_repository.read(tranzactie.id_client)
        if garantie == True:
            if card_client is None:
                suma_piese=0
                tranzactie = Tranzactie(id_tranzactie, id_car, id_client, suma_piese, suma_manopera, data_ora)
                self.__tranzactie_repository.create(tranzactie)
            else:
                suma_piese=0
                suma_manopera = suma_manopera * 0.9
                tranzactie = Tranzactie(id_tranzactie, id_car, id_client, suma_piese, suma_manopera, data_ora)
                self.__tranzactie_repository.create(tranzactie)
        else:
            if card_client is None:
                tranzactie = Tranzactie(id_tranzactie, id_car, id_client, suma_piese, suma_manopera, data_ora)
                self.__tranzactie_repository.create(tranzactie)
            else:
                suma_manopera=suma_manopera*0.9
                tranzactie = Tranzactie(id_tranzactie, id_car, id_client, suma_piese, suma_manopera, data_ora)
                self.__tranzactie_repository.create(tranzactie)



    def get_all(self):
        """
        :return: a list of all the orders, containing Car and Location objects.
        """
        return self.__tranzactie_repository.read()


    def remove_tranzactie(self, id_tranzactie):
        tranzactie_to_delete=self.__tranzactie_repository.read(id_tranzactie)
        if tranzactie_to_delete is not None:
            self.__tranzactie_repository.delete(id_tranzactie)


    def update_tranzactie(self, id_tranzactie,id_car,id_client,suma_piese,suma_manopera,data_ora):
        if self.__car_repository.read(id_car) is None:
            raise ValueError('Nu exista nicio masina cu id-ul: ')
        tranzactie_to_update=self.__tranzactie_repository.read(id_tranzactie)
        if tranzactie_to_update is not None:
            tranzactie=Tranzactie(id_tranzactie,id_car,id_client,suma_piese,suma_manopera,data_ora)
            self.__tranzactie_repository.update(tranzactie)

    def suma(self, x, y):
        from repository.car_repository import CarInMemoryRepository
        lista=[]
        for tranzactie in self.__tranzactie_repository.read():
            tranzactie=self.__tranzactie_repository.read(tranzactie.id_entity)
            id_car=tranzactie.id_car
            car=self.__car_repository.read(tranzactie.id_car)
            garantie=car.garantie
            if garantie==True or garantie=='da':
                suma_pies=0
            else:
                suma_pies=tranzactie.suma_piese
            suma_manoper=tranzactie.suma_manopera
            suma=suma_pies+suma_manoper
            if suma<x and suma>y:
                lista.append(tranzactie.id_entity)
        return lista

    def sortare_manopera(self):
         return sorted(self.get_all(),
            key=lambda tranzactie: tranzactie.suma_manopera,
            reverse=True)

    def sortare_reducere(self, x):

        return sorted(self.get_all(),
                      key=lambda tranzactie: x + tranzactie.suma_manopera/9,
                      reverse=True)

    def date_delete(self, x, y):
        lista=[]
        for tranzactie in self.__tranzactie_repository.read():
            tranzactie=self.__tranzactie_repository.read(tranzactie.id_entity)
            data=tranzactie.data_ora
            id_tranzactie=tranzactie.id_entity
            if data <x and data>y:
                self.__tranzactie_repository.delete(id_tranzactie)
        return self.__tranzactie_repository.read()

    def bubblesort(self):
        lista=[]
        for tranzactie in self.__tranzactie_repository.read():
            tranzactie=self.__tranzactie_repository.read(tranzactie.id_entity)
            id_tranzactie=tranzactie.id_entity
            lista.append(id_tranzactie)
        swapped = True
        count = 1
        while swapped:
            swapped = False
            for i in range(len(lista) - count):
                if lista[i] > lista[i + 1]:
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    swapped = True
            if swapped:
                count += 1
        return lista

    def lista(self):
        lista = []
        for tranzactie in self.__tranzactie_repository.read():
            tranzactie = self.__tranzactie_repository.read(tranzactie.id_entity)
            id_tranzactie = tranzactie.id_entity
            lista.append(tranzactie)
        return lista










