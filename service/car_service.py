from domain.car import Car
from repository.car_repository import CarInMemoryRepository


class CarService:
    """
    Manages car logic.
    """

    def __init__(self, car_repository , repository, validator):
        """
        Creates a car service.
        """
        self.__validator = validator
        self.__repository = repository
        self.__car_repository = car_repository


    def add_car(self, id_car,model,an_cumparare , nr_km, garantie,an_fabricatie ):
        """
        Creates a car
        :param id_car: int, the card id.
        :param indicator: int, the indicator.
        :param comfort_level: str, one of 'standard', 'high', 'premium'
        :param card_payment: bool
        :param model: str, the model
        """
        if garantie =='da':
            garantie = True
        else:
            garantie = False
        car = Car(id_car, model, an_cumparare, nr_km, garantie, an_fabricatie)
        self.__car_repository.create(car)



    def remove_car(self, id_car):
        car_to_delete = self.__car_repository.read(id_car)
        if car_to_delete is not None:
            self.__car_repository.delete(id_car)


    def update_car(self, id_car,model, an_cumparare, nr_km, garantie, an_fabricatie):
        car_to_update=self.__repository.read(id_car)
        if car_to_update is not None:
            car = Car(id_car, model, an_cumparare, nr_km, garantie,an_fabricatie)
            self.__car_repository.update(car)

    def get_all(self):
        """
        :return: a list of all the cars.
        """
        return self.__car_repository.read()



    def garantie(self ):
        import datetime
        for car in self.__car_repository.read():
            car=self.__car_repository.read(car.id_entity)
            nr_km=car.nr_km
            an_cumparare=car.an_cumparare
            id_car=car.id_entity
            model=car.model
            an_fabricatie=car.an_fabricatie
            garantie=car.garantie
            x = datetime.datetime(2016, 12, 12)
            if nr_km<60000 and an_cumparare> x :
                garantie= 'da'
            else:
                garantie= 'nu'
            car = Car(id_car, model, an_cumparare, nr_km, garantie, an_fabricatie)
            self.__car_repository.update(car)

    def cautare(self, x, y, z):
        for car in self.__car_repository.read():
            car=self.__car_repository.read(car.id_entity)
            model=car.model
            an_cumparare=car.an_cumparare
            nr_km=car.nr_km
            an_fabricatie=car.an_fabricatie
            if x==model:
                print(model)
            if y==nr_km:
                print(nr_km)
            if z==an_fabricatie:
                print(an_fabricatie)
