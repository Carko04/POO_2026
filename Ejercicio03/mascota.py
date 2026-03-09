
class Mascota:
    def __init__(self, nombre, tipo, edad, nivelFelicidad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.nivelFelicidad = nivelFelicidad

    def alimentar(self, cantidad):
        self.nivelFelicidad += 10
        self.ajustar_felicidad()

    def jugar(self, tiempo):
        self.nivelFelicidad += 20
        self.ajustar_felicidad()

    def ajustar_felicidad(self):
        if self.nivelFelicidad > 100:
            self.nivelFelicidad = 100

    def es_feliz(self):
        return self.nivelFelicidad >= 70


# Mascota 1
mascota1 = Mascota("Kira", "Perro", 5, 40)
print(f"Nombre: {mascota1.nombre}, Tipo: {mascota1.tipo}, Edad: {mascota1.edad}, Nivel de Felicidad: {mascota1.nivelFelicidad}")
print(f"¿Es feliz? {'Sí' if mascota1.es_feliz() else 'No'}")

mascota1.alimentar(10)
print(f"Nivel de Felicidad después de alimentar: {mascota1.nivelFelicidad}")

mascota1.jugar(20)
print(f"Nivel de Felicidad después de jugar: {mascota1.nivelFelicidad}")


# Mascota 2
mascota2 = Mascota("Mia", "Gato", 3, 60)
print(f"\nNombre: {mascota2.nombre}, Tipo: {mascota2.tipo}, Edad: {mascota2.edad}, Nivel de Felicidad: {mascota2.nivelFelicidad}")
print(f"¿Es feliz? {'Sí' if mascota2.es_feliz() else 'No'}")

mascota2.alimentar(10)
print(f"Nivel de Felicidad después de alimentar: {mascota2.nivelFelicidad}")

mascota2.jugar(20)
print(f"Nivel de Felicidad después de jugar: {mascota2.nivelFelicidad}")

