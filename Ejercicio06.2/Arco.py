from Herramientas import Herramientas

class Arco(Herramientas):

    def __init__(self, material, durabilidad, flechas):
        super().__init__(material, durabilidad)
        self.flechas = flechas

    @property
    def nombre(self):
        return "Arco"

    def usar(self, objetivo: str):

        if self.rota:
            return "El arco está roto."

        if self.flechas <= 0:
            # Si no hay flechas, el arco ya no puede usarse
            self._usos_restantes = 0
            return "Sin flechas"

        daño = self.calcular_daño()
        self.desgastar()
        self.flechas -= 1

        return f"Disparando a {objetivo}. Daño: {daño}. Flechas restantes: {self.flechas}"