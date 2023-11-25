class Automovil:

    def color(sel):
        return "El carro es rojo"
    
class Moto:

    def color(self):
        return "La moto es negra"
    

carro = Automovil()
aveo = carro.color()
print(aveo)

moto = Moto()
yamaha = moto.color()
print(yamaha)