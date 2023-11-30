

""" Creo 3 clases con un metodo actividad para ver el polimorfismo. 
luego una funcion para llamar dicho metodo y aplicarselo a cada clase
 """
class Medico:
    def actividad(self):
        print("Trabajo en hospitales")

class Odontologo:
    def actividad(self):
        print("Trabajo con muelas")

class Ortopedista:
    def actividad(self):
        print("Trabajo con huesos")

def profesion(profesiones):
    profesiones.actividad()

medico = Medico()
odontologo = Odontologo()
ortopedista = Ortopedista()

profesion(medico)
profesion(odontologo)
profesion(ortopedista)
        
