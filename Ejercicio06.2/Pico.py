from Herramientas import Herramientas

class Pico(Herramientas):

    @property
    def nombre(self):
        return "Pico"

    def usar(self, objetivo: str):
        if self.rota:
            return "El pico está roto."

        daño = self.calcular_daño()
        self.desgastar()

        return f"Minando {objetivo}. Daño: {daño}"