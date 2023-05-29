import os
os.system("cls")

# Definiendo una clase
class Persona:
    genero = "Masculino"
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludo(self):
        print(f'Hola, yo soy {self.nombre} y tengo {self.edad} años')

class Estudiante(Persona):
    #Constructor

    def __init__(self, nombre, edad, carrera, semestre):
        #Definiendo los atributos de la clase
        super().__init__(nombre, edad)
        self.carrera = carrera
        self.semestre = semestre
    
    #Definiendo un método
    def saludar(self):
        print(f'Hola, estudio {self.carrera} y voy en {self.semestre} Semestre')


# Crear estancia de la clase Estudiante
oscar = Estudiante("Oscar", 24, "Mecatronica", 10)
# Imprimiento los atributos de la instancia
print(oscar.nombre)
print(oscar.edad)
print(oscar.carrera)
print(oscar.semestre)
#Mandando llamar el método de la clase Estudiante
oscar.saludo()
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


#Otro ejemplo
class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("El perro hace: ¡Guau! ¡Guau!")

class Gato(Animal):
    def hacer_sonido(self):
        print("El gato hace: ¡Miau! ¡Miau!")

class Vaca(Animal):
    def hacer_sonido(self):
        print("La vaca hace: ¡Muu! ¡Muu!")

# Utilizar polimorfismo
animales = [Perro(), Gato(), Vaca()]

for animal in animales:
    animal.hacer_sonido()


# Ultimo ejemplo

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def obtener_salario(self):
        return self.salario

    def mostrar_informacion(self):
        pass

class Gerente(Empleado):
    def __init__(self, nombre, salario, bono):
        super().__init__(nombre, salario)
        self.bono = bono

    def obtener_salario(self):
        return self.salario + self.bono

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}\nSalario: {self.obtener_salario()}")

class Vendedor(Empleado):
    def __init__(self, nombre, salario, comision):
        super().__init__(nombre, salario)
        self.comision = comision

    def obtener_salario(self):
        return self.salario + self.comision

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}\nSalario: {self.obtener_salario()}")

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}\nPrecio: {self.precio}")

class Tienda:
    def __init__(self, nombre, empleados):
        self.nombre = nombre
        self.empleados = empleados

    def mostrar_informacion(self):
        print(f"Tienda: {self.nombre}")
        print("---- Empleados ----")
        for empleado in self.empleados:
            empleado.mostrar_informacion()

# Crear empleados
gerente1 = Gerente("María", 5000, 2000)
vendedor1 = Vendedor("Juan", 3000, 500)

# Crear productos
producto1 = Producto("Camisa", 25.99)
producto2 = Producto("Pantalón", 39.99)

# Crear tienda
tienda = Tienda("Mi Tienda", [gerente1, vendedor1])

# Mostrar información de la tienda
tienda.mostrar_informacion()
print("---- Productos ----")
producto1.mostrar_informacion()
producto2.mostrar_informacion()