from Mob import Mob

class Creeper(Mob):
    """Mob agresivo, suena '...Ssssss', corre hacia el jugador."""

    def hacer_sonido(self):
        return "...Ssssss"

    def comportamiento(self):
        return "Agresivo"

    def moverse(self):
        return "Corre silenciosamente hacia el jugador"