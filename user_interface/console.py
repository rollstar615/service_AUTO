from domain.car import Car
from repository.repository_error import RepositoryError
from repository.tranzactie_repository import TranzactieInMemoryRepository
from datetime import datetime
from datetime import date

class Console:

    def __init__(self, car_service, card_client_service, tranzactie_service):
        self.__car_service = car_service
        self.__card_client_service = card_client_service
        self.__tranzactie_service = tranzactie_service

    def __show_menu(self):
        print('1. Masini')
        print('2. Clienti')
        print('3. Tranzactii')
        print('x. Exit')

    def run_console(self):

        while True:
            self.__show_menu()
            op = input('Optiune: ')
            if op == '1':
                self.__show_masini()
            elif op == '2':
                self.__show_clienti()
            elif op == '3':
                self.__show_tranzactii()
            elif op == 'x':
                break
            else:
                print('Comanda invalida!')

    def __show_masini(self):

        while True:
            self.__show_menu_masini()
            op = input('Optiune: ')
            if op == '1':
                self.__handle_masini_add()
            elif op == '2':
                self.__handle_masini_remove()
            elif op=='3':
                self.__handle_car_update()
            elif op =='4':
                x=input('litere')
                y=int(input('ceva'))
                z=datetime.strptime(input('Enter Start date in the format m/d/y'), '%m/%d/%Y')
                print((self.__car_service.cautare(x,y,z)))
            elif op == '5':
                self.__car_service.garantie()
            elif op== '6':
                self.__car_service.garantie1()
            elif op == 'a':
                self.__show_list(self.__car_service.get_all())
            elif op == 'b':
                break
            else:
                print('Comanda invalida!')

    def __show_menu_masini(self):
        print('--- Masini')
        print('1. Adauga')
        print('2. Sterge')
        print('3. Update')
        print('4.Cautare')
        print('5.Garantie')
        print('6.Garantie1')
        print('a. Afisare')
        print('b. Back')

    def __handle_masini_add(self):
        try:
            id_car = int(input('ID-ul: '))
            model = input('model: ')
            an_cumparare = datetime.strptime(input('Enter Start date in the format m/d/y'), '%m/%d/%Y')
            nr_km = int(input('nr de km: '))
            garantie = input('garantie: ')
            an_fabricatie=datetime.strptime(input('Enter Start date in the format m/d/y'), '%m/%d/%Y')
            self.__car_service.add_car(
                id_car,
                model,
                an_cumparare,
                nr_km,
                garantie,
                an_fabricatie
            )
            print('Masina a fost adaugata!')
        except RepositoryError as re:
            print('Eroare:', re)

            #print('Avem erori:', ve)

    def __show_list(self, objects):
        for object in objects:
            print(object)

    def __show_clienti(self):
        while True:
            self.__show_menu_clienti()
            op = input('Optiune: ')
            if op == '1':
                self.__handle_clienti_add()
            if op=='2':
                self.__handle_clienti_remove()
            elif op=='3':
                self.__handle_clienti_update()
            elif op=='4':
                x=input('text')
                y=int(input('numar'))
                z=datetime.strptime(input('Enter Start date in the format m/d/y'), '%m/%d/%Y')
                print((self.__card_client_service.cautare2(x, y, z)))
            elif op=='5':
                self.__show_list(self.__card_client_service.cnp())
            elif op == 'a':
                self.__show_list(self.__card_client_service.get_all())
            elif op == 'b':
                break
            else:
                print('Comanda invalida!')

    def __show_menu_clienti(self):
        print('--- Locatii')
        print('1. Adauga')
        print('2. Sterge')
        print('3. Update')
        print('4.CAUTARE')
        print('a. Afisare')
        print('b. Back')

    def __handle_clienti_add(self):
        try:
            id_client = int(input('ID-ul: '))
            nume= input('nume: ')
            prenume = input('prenume: ')
            cnp = int(input('cnp: '))
            data_nasterii = datetime.strptime(input('Enter Start date in the format m/d/y'), '%m/%d/%Y')
            data_inregistrarii = datetime.strptime(input('Enter Start date in the format m/d/y'), '%m/%d/%Y')
            self.__card_client_service.add_client(
                id_client,
                nume,
                prenume,
                cnp,
                data_nasterii,
                data_inregistrarii
            )
            print('Locatia a fost adaugata!')
        except RepositoryError as re:
            print('Eroare:', re)


    def __show_tranzactii(self):
        while True:
            self.__show_menu_comenzi()
            op = input('Optiune: ')
            if op == '1':
                self.__handle_tranzactii_add()
            elif op=='2':
                self.__handle_tranzactii_remove()
            elif op=='3':
                self.__handle_tranzactii_update()
            elif op=='4':
                self.__handle_reducere()
            elif op=='5':
                self.__handle_suma()
            elif op=='6':
                self.__show_list(self.__tranzactie_service.sortare_manopera())
            elif op=='7':
                x=int(input('reducerea este '))
                self.__show_list(self.__tranzactie_service.sortare_reducere(x))
            elif op=='8':
                self.__handle_date()
            elif op=='9':
                print(self.__tranzactie_service.bubblesort())
            elif op=='10':
                print(self.__tranzactie_service.lista())
            elif op == 'a':
                self.__show_list(self.__tranzactie_service.get_all())
            elif op == 'b':
                break
            else:
                print('Comanda invalida!')

    def __show_menu_comenzi(self):
        print('--- Comenzi')
        print('1. Adauga')
        print('2. Sterge')
        print('3. Update')
        print('4.Reducere')
        print('5.Interval')
        print('6.Sortare')
        print('7.Sortare2')
        print('8.Interval data')
        print('9.Bubblesort')
        print('10.Lista')
        print('a. Afisare')
        print('b. Back')

    def __handle_tranzactii_add(self):
        try:
            id_tranzactie = int(input('ID-ul comenzii: '))
            id_car = int(input('ID-ul masinii: '))
            id_client = int(input('ID-ul client '))
            suma_piese = int(input('suma piese '))
            suma_manopera = float(input('suma manopera'))
            data_ora =datetime.strptime(input('Enter Start date in the format m/d/y'), '%m/%d/%Y')
            self.__tranzactie_service.add_tranzactie(
                id_tranzactie,
                id_car,
                id_client,
                suma_piese,
                suma_manopera,
                data_ora)
            print('a fost adaugat')
        except ValueError as ve:
            print('Erori:')
            for error in ve.args[0]:
                print(error)

    def __handle_masini_remove(self):
        try:
            id_car = int(input('Dati id-ul de sters: '))
            self.__car_service.remove_car(id_car)
        except Exception:
            print('TODO better exception handling')

    def __handle_clienti_remove(self):
        try:
            id_client = int(input('dati idul de sters'))
            self.__card_client_service.remove_client(id_client)
        except Exception:
            self.__card_client_service.remove_client(id_client)

    def __handle_tranzactii_remove(self):
        try:
            id_tranzactie=int(input('dati idul de sters'))
            self.__tranzactie_service.remove_tranzactie(id_tranzactie)
        except Exception:
            self.__tranzactie_service.remove_tranzactie(id_tranzactie)

    def __handle_car_update(self):
            id_car=int(input('dati idul'))
            model=input('dati modelul')
            an_cumparare=datetime.strptime(input('Enter Start date in the format m/d/y'), '%m/%d/%Y')
            nr_km=int(input('dati km'))
            garantie=input('dati garantia')
            an_fabricatie=datetime.strptime(input('Enter Start date in the format m/d/y'), '%m/%d/%Y')
            self.__car_service.update_car(
                id_car,
                model,
                an_cumparare,
                nr_km,
                garantie,
                an_fabricatie
            )
            print('Masina a fost adaugata!')

    def __handle_clienti_update(self):
        id_client = int(input('ID-ul: '))
        nume = input('nume: ')
        prenume = input('prenume: ')
        cnp = int(input('cnp: '))
        data_nasterii = datetime.strptime(input('Enter Start date in the format m/d/y'), '%m/%d/%Y')
        data_inregistrarii = datetime.strptime(input('Enter Start date in the format m/d/y'), '%m/%d/%Y')
        self.__card_client_service.update_client(
            id_client,
            nume,
            prenume,
            cnp,
            data_nasterii,
            data_inregistrarii
        )
        print('locatia a fost modificata')

    def __handle_tranzactii_update(self):
        id_tranzactie=int(input('dati orderul'))
        id_car=int(input('dati masina'))
        id_client=int(input('dati client'))
        suma_piese=int(input('dati suma piese'))
        suma_manopera=int(input('dati suma manopera'))
        data_ora= datetime.strptime(input('Enter Start date in the format m/d/y'), '%m/%d/%Y')

        self.__tranzactie_service.update_tranzactie(
            id_tranzactie,
            id_car,
            id_client,
            suma_piese,
            suma_manopera,
            data_ora
        )
        print('orderul a fost actualizat')

    from repository.tranzactie_repository import TranzactieInMemoryRepository
    def __handle_reducere(self):
        self.__show_list(self.__tranzactie_service.sortare_reducere(x))

    def __handle_suma(self):
        x=int(input('capatul de sus'))
        y=int(input('capatul de jos'))
        print( self.__tranzactie_service.suma(x,y))
        print(' s a facut')

    def __handle_date(self):
        y= datetime.strptime(input('Enter Start date in the format m/d/y'), '%m/%d/%Y')
        x=datetime.strptime(input('Enter end date in the format m/d/y'), '%m/%d/%Y')
        print(self.__tranzactie_service.date_delete(x,y))
        print('realizat')