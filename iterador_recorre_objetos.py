# Crea un iterador que recorra los siguientes objetos: palabra, lista, tupla y muestre en pantalla (print()) para cada uno de ellos su longitud con la función len().

# Definir los objetos
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

# Recorrer los tres objetos en un solo bucle
for objeto in (palabra, lista, tupla):
    if isinstance(objeto, str):
        print("Longitud de la cadena:", len(objeto))
    elif isinstance(objeto, list):
        print("Longitudes de la lista:")
        for elemento in objeto:
            print(len(elemento))
    elif isinstance(objeto, tuple):
        print("Longitudes de la tupla:")
        for elemento in objeto:
            print(len(str(elemento)))
    else:
        print("Tipo de objeto no reconocido")
