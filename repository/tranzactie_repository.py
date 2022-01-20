from repository import car_repository
class TranzactieInMemoryRepository:
    '''
    Repository for storing data in memory
    '''

    def __init__(self):
        '''
        Creates an in memory repository.
        '''
        self.__storage = {}

    # metode CRUD
    # CRUD = Create
    #        Read
    #        Update
    #        Delete

    def create(self, tranzactie):
        '''
        Adds a new order.
        :param order: the given order
        :return: -
        :raises: KeyError if the id already exists
        '''
        tranzactie_id = tranzactie.id_tranzactie
        if tranzactie_id in self.__storage:
            raise KeyError('The order id already exists!')
        self.__storage[tranzactie_id] = tranzactie

    def read(self, tranzactie_id=None):
        '''
        Gets a order by id or all the orders
        :param order_id: optional, the order id
        :return: the list of orders or the order with the given id
        '''
        if tranzactie_id is None:
            return self.__storage.values()

        if tranzactie_id in self.__storage:
            return self.__storage[tranzactie_id]
        return None


    def update(self, tranzactie):
        '''
        Updates order.
        :param order: the order to update
        :return: -
        :raises: KeyError if the id does not exist
        '''
        tranzactie_id = tranzactie.id_tranzactie
        if tranzactie_id not in self.__storage:
            raise KeyError('There is no order with that id!')
        self.__storage[tranzactie_id] = tranzactie

    def delete(self, tranzactie_id):
        '''
        Deletes a order.
        :param order_id: the order id to delete.
        :return: -
        :raises KeyError: if no order with order_id
        '''
        if tranzactie_id not in self.__storage:
            raise KeyError('There is no order with that id!')
        del self.__storage[tranzactie_id]

    def clear(self):
        self.__storage.clear()