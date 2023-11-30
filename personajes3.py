""" Tienes tres clases de personajes en un juego, los cuales cuentan con sus métodos de defensa específicos.

Crea una función llamada personaje_defender(), que pueda recibir un objeto (una instancia de las clases de tus personajes), y ejecutar su método defender() independientemente de qué tipo de persona
Crea una función llamada personaje_defender(), que pueda recibir un objeto (una instancia de las clases de tus personajes), y ejecutar su método defender() independientemente de qué tipo de personaje se trate. """

# Definición de las clases de personajes
class Mago:
    def defender(self):
        print("Escudo mágico")

class Arquero:
    def defender(self):
        print("Esconderse")

class Samurai:
    def defender(self):
        print("Bloqueo")

# Definición de la función personaje_defender()
def personaje_defender(personaje):
    personaje.defender()

# Crear instancias de las clases de personajes
mago = Mago()
arquero = Arquero()
samurai = Samurai()

# Llamar a la función personaje_defender() para cada tipo de personaje
personaje_defender(mago)
personaje_defender(arquero)
personaje_defender(samurai)


