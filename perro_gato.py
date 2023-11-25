class Perro:
    def hablar(self):
        return "Guau"

class Gato:
    def hablar(self):
        return "Meow"

# Crear una instancia de la clase Perro
mi_perro = Perro()

# Llamar al método hablar de la clase Perro
sonido_perro = mi_perro.hablar()

# Crear una instancia de la clase Gato
mi_gato = Gato()

# Llamar al método hablar de la clase Gato
sonido_gato = mi_gato.hablar()

# Imprimir los sonidos
print("El perro dice:", sonido_perro)
print("El gato dice:", sonido_gato)
