class Futbolista:
    def golpear(self):
        print("Patea al arco")

class Tenista:
    def golpear(self):
        print("golpea la pelota")

class Baloncesto:
    def golpear(self):
        print("Golpea el balon de basket")

futbolista = Futbolista()
tenista = Tenista()
baloncesto = Baloncesto()

jugadores = [futbolista,tenista,baloncesto]

for jugador in jugadores:
    jugador.golpear()