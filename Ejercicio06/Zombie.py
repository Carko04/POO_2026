from Mob import Mob

class Zombie(Mob):
    """Mob agresivo que camina lentamente."""

    def hacer_sonido(self):
        return "Grrrrr"

    def comportamiento(self):
        return "Agresivo"

    def moverse(self):
        return "Camina lentamente buscando jugadores"
