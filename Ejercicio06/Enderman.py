from Mob import Mob

class Enderman(Mob):
    """Mob neutral, sonido distorsionado, se teletransporta."""

    def hacer_sonido(self):
        return "Ruidos distorsionados"

    def comportamiento(self):
        return "Neutral"

    def moverse(self):
        return "Se teletransporta de un lugar a otro"