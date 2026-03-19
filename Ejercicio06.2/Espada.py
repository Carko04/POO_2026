from Herramientas import Herramientas

class Espada(Herramientas):

    @property
    def nombre(self):
        return "Espada"

    def usar(self, objetivo: str):
        if self.rota:
            return "La espada está rota."

        daño = self.calcular_daño()
        self.desgastar()

        return f"Atacando a {objetivo}. Daño: {daño}"