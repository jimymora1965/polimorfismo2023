class Ave:
    def hacer_sonido(self):
        pass

class Pato(Ave):
    def hacer_sonido(self):
        return "Cuack"

class Gorrion(Ave):
    def hacer_sonido(self):
        return "Chirp"

def hacer_sonido_de_ave(ave):
    return ave.hacer_sonido()

# Uso de polimorfismo
pato = Pato()
gorrion = Gorrion()

print(pato.hacer_sonido())    # Resultado: Cuack. Se puede llamar al metodo asi 
print(hacer_sonido_de_ave(gorrion)) # Resultado: Chirp ó Así
