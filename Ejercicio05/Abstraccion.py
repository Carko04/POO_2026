from abc import ABC, abstractmethod

#Clase abstracta (plantilla)
class Animal (ABC):

 @abstractmethod
 def hablar(self):
    pass # No se implementa el método


# Clase en especifico
class Perro(Animal):
    def hablar(self):
        return "Woof!"

# Clase en especifico

class Gato(Animal):
    def hablar(self):
        return "Meow!"


# usar las clases 
perro = Perro()
gato = Gato()

print(perro.hablar())
print(gato.hablar())