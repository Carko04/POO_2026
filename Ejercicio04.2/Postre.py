from Platillo import Platillo

class Postre(Platillo):
    def __init__(self, nombre, precio, calorias):
        super().__init__(nombre, precio)
        self.calorias = calorias
        
    def mostrarInformacion(self):
        super().mostrarInfo()
        print(f"Calorias: {self.calorias}")