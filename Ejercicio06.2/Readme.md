# Sistema de Herramientas

Este código implementa un sistema de herramientas en Python utilizando **Programación Orientada a Objetos**. La clase abstracta `Herramientas` define las propiedades y comportamientos comunes, como el **material, la durabilidad, el cálculo de daño y el desgaste** al utilizar la herramienta.

A partir de esta clase se crean herramientas específicas como `Pico`, `Espada`, `Pala` y `Arco`. Cada una implementa el método `usar()` y la propiedad `nombre`, lo que permite que todas puedan ser utilizadas de manera uniforme en el programa principal.

El archivo `main.py` instancia varias herramientas y simula su uso contra un objetivo. Durante la ejecución se muestra el daño causado, los usos restantes y el estado de cada herramienta hasta que deja de utilizarse o se rompe.

El propósito del código es demostrar el uso de **herencia, clases abstractas y polimorfismo**, permitiendo que diferentes tipos de herramientas compartan una misma estructura base mientras mantienen comportamientos propios.
