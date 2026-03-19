from Mob import Mob

class Vaca(Mob):
    """Mob pasivo, suena 'Muuuu', camina lento."""

    def hacer_sonido(self):
        return "Muuuu"

    def comportamiento(self):
        return "Pasivo"

    def moverse(self):
        return "Camina lentamente por el pasto"