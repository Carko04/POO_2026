from Comida import Comida
from Bebida import Bebida
from Postre import Postre

comida1 = Comida("Hamburguesa", 80, "Comida rapida")
bebida1 = Bebida("Refresco", 25, "Frio")
postre1 = Postre("Pastel", 40, 300)

print("---- COMIDA ----")
comida1.mostrarInformacion()

print("\n---- BEBIDA ----")
bebida1.mostrarInformacion()

print("\n---- POSTRE ----")
postre1.mostrarInformacion()