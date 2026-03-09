from Guerrero import Guerrero
from Mago import Mago
from Arquero import Arquero

# Crear personajes
guerrero = Guerrero("Thorin", 10, "Espada")
mago = Mago("Merlín", 12, "Bola de fuego")
arquero = Arquero("Legolas", 9, 20)

# Guerrero
guerrero.presentarse()
guerrero.usar_habilidad()

print()

# Mago
mago.presentarse()
mago.usar_habilidad()

print()

# Arquero
arquero.presentarse()
arquero.usar_habilidad()