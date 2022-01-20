from repository.GenericFileRepository import GenericFileRepository
from repository.car_repository import CarInMemoryRepository
from repository.card_client_repository import ClientInMemoryRepository
from repository.tranzactie_repository import TranzactieInMemoryRepository
from service.car_service import CarService
from service.card_client_service  import ClientService
from service.tranzactie_service import TranzactieService
from user_interface.console import Console
from domain.validator import CarValidator

car_repository = CarInMemoryRepository()
card_client_repository = ClientInMemoryRepository
tranzactie_repository = TranzactieInMemoryRepository()
car_repository = GenericFileRepository('cars.pkl')
card_client_repository = GenericFileRepository('clienti.pkl')
tranzactie_repository = GenericFileRepository('tranzactii.pkl')
validato=CarValidator()
validator=0

car_service = CarService(car_repository, tranzactie_repository, validator)
card_client_service = ClientService(card_client_repository)
tranzactie_service = TranzactieService(tranzactie_repository, car_repository, card_client_repository)
#
# car_service.add_car(1, '1', 'high', 'da', '1234')
# location_service.add_location(1, 'kogalniceanu', 1, 1, 1, 'nimic')
# location_service.add_location(2, 'rebreanu', 2, 2, 2, 'nimic 2')
# order_service.add_order(1, 1, 1, 20, 3, 10, 'done')
# order_service.add_order(2, 1, 1, 20, 3, 7, 'done')
# order_service.add_order(3, 1, 1, 20, 3, 12, 'done')
# order_service.add_order(4, 1, 2, 20, 3, 20, 'done')
# order_service.add_order(50, 1, 2, 20, 3, 14, 'done')

console = Console(car_service, card_client_service,tranzactie_service)
console.run_console()

