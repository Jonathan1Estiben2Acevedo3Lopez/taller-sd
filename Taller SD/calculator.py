from Pyro5.api import expose

@expose   # muy importante: está sobre la clase, no sobre cada método
class CalculatorService(object):
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        return a / b
