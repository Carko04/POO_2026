class Platillo:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
    def mostrarInfo(self):
        print(f"Nombre del platillo: {self.nombre}")
        print(f"Precio: ${self.precio}")