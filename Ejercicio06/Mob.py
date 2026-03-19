
from abc import ABC, abstractmethod

class Mob(ABC):
    """Clase abstracta base para todos los mobs."""

    def __init__(self, nombre: str, vida: int):
        self.nombre = nombre
        self.vida   = vida

    # Métodos ABSTRACTOS

    @abstractmethod
    def hacer_sonido(self) -> str:
        pass

    @abstractmethod
    def comportamiento(self) -> str:
        pass

    @abstractmethod
    def moverse(self) -> str:
        pass

    # Método concreto

    def presentarse(self):
        print(f"=== {self.nombre} ===")
        print(f"❤️  Vida       : {self.vida} HP")
        print(f"🔊  Sonido     : {self.hacer_sonido()}")
        print(f"⚔️  Tipo       : {self.comportamiento()}")
        print(f"🏃  Movimiento : {self.moverse()}")
        print()

