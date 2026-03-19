from Pico import Pico
from Espada import Espada
from Pala import Pala
from Arco import Arco

herramientas = [
    Pico("diamante", 3),
    Espada("hierro", 2),
    Pala("madera", 2),
    Arco("oro", 3, 2)
]

objetivos = ["mena de diamante", "Creeper", "arena", "zombie"]

for h in herramientas:

    print(f"\nUsando {h.nombre}:")

    while not h.rota:
        print(h.usar(objetivos[herramientas.index(h)]))
        h.estado()

    # detener si es un arco sin flechas
        if hasattr(h, "flechas") and h.flechas == 0:
            print("El arco ya no tiene flechas.\n")
            break

    if h.rota:
        print("La herramienta se rompió.\n")
    else:
        print("La herramienta dejó de usarse.\n")