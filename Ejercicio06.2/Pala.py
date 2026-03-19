from Herramientas import Herramientas

class Pala(Herramientas):

    @property
    def nombre(self):
        return "Pala"

    def usar(self, objetivo: str):
        if self.rota:
            return "La pala está rota."

        daño = self.calcular_daño()
        self.desgastar()

        return f"Excavando {objetivo}. Daño: {daño}"