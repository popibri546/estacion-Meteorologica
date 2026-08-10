import random

class Sensor:
    def __init__(self, nombre, pin):
        self.nombre = nombre  # Atributo
        self.pin = pin        # Atributo
        self.valor = 0        # Atributo inicial

    def tomar_lectura(self):
        self.valor = random.randint(10, 40)
        print(f"Sensor {self.nombre} (Pin {self.pin}) leyendo... Valor: {self.valor}")
