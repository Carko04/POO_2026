from Vaca import Vaca
from Creeper import Creeper
from Enderman import Enderman
from Zombie import Zombie

    # Mostrar información de cada mob    print("Información de los mobs en Minecraft:\n")
vaca = Vaca("Bessie", 10)
creeper = Creeper("Explosi", 20)
enderman = Enderman("Tall Boi", 40)
zombie = Zombie("Brainless", 30)

print("Vaca:")
vaca.presentarse()
    
print("Creeper:")
creeper.presentarse()
    
print("Enderman:")
enderman.presentarse()
    
print("Zombie:")
zombie.presentarse()