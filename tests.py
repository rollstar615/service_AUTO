from domain.car import Car
from service.car_service import CarService


def test_car_service():

    car_service = CarService()
    car = Car(1, 12, 'premium', True, 'e46')
    car_service.add_car(car.id_car,
                        car.model,
                        car.nr_km,
                        car.an_cumparare,
                        car.an_fabricatie)
    assert car_service.get_all() == [car]

    try:
        car_service.add_car(car.id_car,
                            car.model,
                            car.nr_km,
                            car.an_cumparare
                            car.an_fabricatie)
        assert False
    except KeyError:
        assert True

test_car_service()


from domain.card_client import Client
from service.card_client_service import ClientService
def test_client_service():

    client_service = ClientService()
    client = Client(1, 333, 123312, 01/01/2000, 01/01/2001)
    client_service.add_client(client.id_client,
                        client.nume,
                        client.cnp,
                        client.data_nasterii,
                        client.data_inregistrarii)
    assert client_service.get_all() == [client]

    try:
        client_service.add_client(client.id_client,
                            client.nume,
                            client.cnp,
                            client.data_nasterii
                            client.data_inregistrarii)
        assert False
    except KeyError:
        assert True

test_client_service()