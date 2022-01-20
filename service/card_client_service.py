from domain.card_client import  Client
from repository.card_client_repository import ClientInMemoryRepository


class ClientService:

    """
    Manages location logic.
    """

    def __init__(self ,card_client_repository):
        """
        Creates a location service.
        """
        self.__card_client_repository=card_client_repository

    def add_client(self, id_client, nume, prenume, cnp, data_nasterii, data_inregistrarii):
        client = Client(id_client, nume, prenume, cnp, data_nasterii,data_inregistrarii)
        #self.__validator.validate(location)
        self.__card_client_repository.create(client)

    def get_all(self):
        """
        :return: a list of all the cars.
        """
        return self.__card_client_repository.read()

    def remove_client(self, id_client):
        client_to_delete = self.__card_client_repository.read(id_client)
        if client_to_delete is not None:
            self.__card_client_repository.delete(id_client)

    def update_client(self, id_client,nume, prenume, cnp,data_nasterii, data_inregistrarii):
        client_to_update=self.__card_client_repository.read(id_client)
        if client_to_update is not None:
            client = Client(id_client, nume, prenume, cnp, data_nasterii, data_inregistrarii)
            self.__card_client_repository.update(client)

    def cautare2(self, x, y, z):
        lista=[]
        for card_client in self.__card_client_repository.read():
            card_client=self.__card_client_repository.read(card_client.id_entity)
            nume=card_client.nume
            prenume=card_client.prenume
            cnp=card_client.prenume
            data_nasterii=card_client.data_nasterii
            if x==nume:
                print(nume)
            if y==cnp:
                print(cnp)
            if x==prenume:
                print(prenume)
            if z==data_nasterii:
                print(data_nasterii)

    def cnp(self):
        r=0
        for card_client in self.__card_client_repository.read():
            client=self.__card_client_repository.read(card_client.id_entity)
            cnpe=client.cnp
            for card_client in self.__card_client_repository.read():
                card_client=self.__card_client_repository.read(card_client.id_entity)
                id=card_client.id_entity
                cnp=card_client.cnp
                if cnp == cnpe:
                    r=r+1
            if r>1:
                self.__card_client_repository.delete(id)
        return self.__card_client_repository.read()
