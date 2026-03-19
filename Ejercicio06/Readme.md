# Mobs del Overworld – Abstracción en POO
## Descripción

Este proyecto muestra el uso de clases abstractas en Python para aplicar el concepto de abstracción en Programación Orientada a Objetos. Se modelan diferentes mobs del universo de Minecraft, donde todos comparten características básicas pero cada uno tiene comportamientos propios.

## Estructura

### Se utiliza una clase abstracta Mob que define:

Atributos comunes: nombre y vida

Métodos abstractos: hacer_sonido(), comportamiento() y moverse()

Un método concreto presentarse() que muestra la información del mob.

# Mobs implementados

Vaca (pasivo)

Creeper (agresivo)

Enderman (neutral)

Zombie (bonus)

## Nota

La clase Mob no puede instanciarse directamente porque contiene métodos abstractos que deben implementarse en sus subclases.