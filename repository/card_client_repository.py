from repository.repository_error import RepositoryError


class ClientInMemoryRepository:
    '''
    Repository for storing data in memory
    '''

    def __init__(self):
        '''
        Creates an in memory repository.
        '''
        self.__storage = {}


    def create(self, card_client):
        '''
        Adds a new location.
        :param location: the given location
        :return: -
        :raises: KeyError if the id already exists
        '''
        client_id =card_client.id_client
        if client_id in self.__storage:
            raise RepositoryError('The location id already exists!')
        self.__storage[client_id] = card_client

    def read(self, client_id=None):
        '''
        Gets a location by id or all the locations
        :param location_id: optional, the location id
        :return: the list of locations or the location with the given id
        '''
        self.__load_from_file(clienti.pkl)
        if client_id is None:
            return self.__storage.values()

        if client_id in self.__storage:
            return self.__storage[client_id]
        return None

    def update(self, card_client):
        '''
        Updates location.
        :param location: the location to update
        :return: -
        :raises: KeyError if the id does not exist
        '''
        client_id = card_client.id_client
        if client_id not in self.__storage:
            raise RepositoryError('There is no location with that id!')
        self.__storage[client_id] = card_client

    def delete(self, client_id):
        '''
        Deletes a location.
        :param location_id: the location id to delete.
        :return: -
        :raises KeyError: if no location with location_id
        '''
        if client_id not in self.__storage:
            raise RepositoryError('There is no location with that id!')
        del self.__storage[client_id]

    def clear(self):
        self.__storage.clear()





