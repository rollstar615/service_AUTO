class TranzactieViewModel:

    def __init__(self, tranzactie, car, client):

        self.order = tranzactie
        self.car = car
        self.location = client

    def __str__(self):
        return '{}. car: {} -- client: {}'.format(
            self.order.id_entity,
            self.car,
            self.client
        )