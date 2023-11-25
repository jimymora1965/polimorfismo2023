class HistoriaClinica:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

    def imprimir_informacion(self):
        pass  # Este método se implementará en las clases derivadas

class Paciente(HistoriaClinica):
    def __init__(self, nombre, edad, genero, antecedentes_medicos=None):
        super().__init__(nombre, edad, genero)
        self.antecedentes_medicos = antecedentes_medicos or []

    def agregar_antecedente_medico(self, antecedente):
        self.antecedentes_medicos.append(antecedente)

    def imprimir_informacion(self):
        print("Historia Clínica de", self.nombre)
        print("Edad:", self.edad)
        print("Género:", self.genero)
        print("Antecedentes Médicos:")
        for antecedente in self.antecedentes_medicos:
            print("-", antecedente)

class Doctor(HistoriaClinica):
    def __init__(self, nombre, especialidad):
        super().__init__(nombre, None, None)
        self.especialidad = especialidad

    def imprimir_informacion(self):
        print("Perfil del Doctor:")
        print("Nombre:", self.nombre)
        print("Especialidad:", self.especialidad)

# Solicitar información al usuario
nombre_paciente = input("Ingrese el nombre del paciente: ")
edad_paciente = int(input("Ingrese la edad del paciente: "))
genero_paciente = input("Ingrese el género del paciente: ")

paciente = Paciente(nombre=nombre_paciente, edad=edad_paciente, genero=genero_paciente)

antecedentes_medicos = input("Ingrese antecedentes médicos del paciente (separados por coma): ").split(',')
paciente.agregar_antecedente_medico(antecedentes_medicos)

nombre_doctor = input("Ingrese el nombre del doctor: ")
especialidad_doctor = input("Ingrese la especialidad del doctor: ")

doctor = Doctor(nombre=nombre_doctor, especialidad=especialidad_doctor)

# Imprimir información utilizando el polimorfismo
historias_clinicas = [paciente, doctor]           

for historia_clinica in historias_clinicas:
    historia_clinica.imprimir_informacion()
    print("\n")
