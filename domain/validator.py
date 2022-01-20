class CarValidationError(Exception):
    pass

class CarValidator:

    def validate(self, car):

        errors = []
        if car.garantie not in ['da', 'nu']:
            errors.append('rrrr')

        if errors != []:
            raise CarValidationError(errors)