# Definiendo una clase
class Estudiante:
    #Constructor

    def __init__(self, carrera, semestre):
        #Definiendo los atributos de la clase
        self.carrera = carrera
        self.semestre = semestre
    
    #Definiendo un método
    def saludar(self):
        print(f'Hola, estudio {self.carrera} y voy en {self.semestre} Semestre')


# Crear estancia de la clase Estudiante
oscar = Estudiante("Mecatronica", 10)
# Imprimiento los atributos de la instancia
print(oscar.carrera)
print(oscar.semestre)
#Mandando llamar el método de la clase Estudiante
oscar.saludar()

#Practica
class Maestro:
    def __init__(self, area, materia):
        self.area = area
        self.materia = materia

    def despedida(self):
        print(f'Hola, soy maestro del area {self.area} y doy clase de {self.materia}')

ruben =  Maestro(3,'Economia')
ruben.despedida()

# Encapusulacion
class Ingeniero:
    def __init__(self, tipo, especialidad):
        # Se ocultan los atributos
        self._tipo = tipo
        self._especialidad = especialidad
    
    # Metodos de acceso getters
    def get_tipo(self):
        return self._tipo
    def get_especialidad(self):
        return self._especialidad

    # Metodos de acceso setters
    def set_tipo(self, nuevo_tipo):
        self._tipo = nuevo_tipo
    
    def set_especialidad(self, nueva_especialidad):
        self._especialidad = nueva_especialidad


marco = Ingeniero('Software','Datos')
print(marco.get_tipo())
print(marco.get_especialidad())

marco.set_tipo('Mecatronica')
marco.set_especialidad('PLC')

print(marco.get_tipo())
print(marco.get_especialidad())


