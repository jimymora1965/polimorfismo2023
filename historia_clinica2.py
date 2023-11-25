class HistoriaClinica:
    def __init__(self, nombre, edad, genero, num_documento, religion, estado_civil, direccion, telefono_contacto, num_contacto_familiar):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.num_documento = num_documento
        self.religion = religion
        self.estado_civil = estado_civil
        self.direccion = direccion
        self.telefono_contacto = telefono_contacto
        self.num_contacto_familiar = num_contacto_familiar

    def imprimir_informacion(self):
        pass  # Este método se implementará en las clases derivadas

class Paciente(HistoriaClinica):
    def __init__(self, nombre, edad, genero, num_documento, religion, estado_civil, direccion, telefono_contacto, num_contacto_familiar, antecedentes_medicos=None):
        super().__init__(nombre, edad, genero, num_documento, religion, estado_civil, direccion, telefono_contacto, num_contacto_familiar)
        self.antecedentes_medicos = antecedentes_medicos or []

    def agregar_antecedente_medico(self, antecedente):
        self.antecedentes_medicos.append(antecedente)

    def imprimir_informacion(self):
        print("Historia Clínica de", self.nombre)
        print("Número de Documento:", self.num_documento)
        print("Edad:", self.edad)
        print("Género:", self.genero)
        print("Religión:", self.religion)
        print("Estado Civil:", self.estado_civil)
        print("Dirección:", self.direccion)
        print("Teléfono de Contacto:", self.telefono_contacto)
        print("Número de Contacto de Familiar o Amigo:", self.num_contacto_familiar)
        print("Antecedentes Médicos:")
        for antecedente in self.antecedentes_medicos:
            print("-", antecedente)

# Solicitar información al usuario
nombre_paciente = input("Ingrese el nombre del paciente: ")
edad_paciente = int(input("Ingrese la edad del paciente: "))
genero_paciente = input("Ingrese el género del paciente: ")
num_documento_paciente = input("Ingrese el número de documento del paciente: ")
religion_paciente = input("Ingrese la religión del paciente: ")
estado_civil_paciente = input("Ingrese el estado civil del paciente: ")
direccion_paciente = input("Ingrese la dirección del paciente: ")
telefono_contacto_paciente = input("Ingrese el teléfono de contacto del paciente: ")
num_contacto_familiar_paciente = input("Ingrese el número de contacto de un familiar o amigo del paciente: ")

paciente = Paciente(
    nombre=nombre_paciente, 
    edad=edad_paciente, 
    genero=genero_paciente, 
    num_documento=num_documento_paciente, 
    religion=religion_paciente, 
    estado_civil=estado_civil_paciente, 
    direccion=direccion_paciente, 
    telefono_contacto=telefono_contacto_paciente, 
    num_contacto_familiar=num_contacto_familiar_paciente
)

antecedentes_medicos = input("Ingrese antecedentes médicos del paciente (separados por coma): ").split(',')
paciente.agregar_antecedente_medico(antecedentes_medicos)

# Imprimir información utilizando el polimorfismo
historias_clinicas = [paciente]

for historia_clinica in historias_clinicas:
    historia_clinica.imprimir_informacion()
    print("\n")
