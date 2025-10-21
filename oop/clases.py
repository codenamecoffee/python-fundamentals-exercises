# A class is like having the - blueprints - of something
# to later be able to - create - it.

class ClaseTipada:
    def _init_ (self, edad: int, name: str):
        pass

class Persona: 

    # Constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre   
        self.edad = edad 

    # - nombre and edad are called "attributes"
    # - They are probably automatically generated properties like in C#
    # because they are being initialized, but do not exist in the class as fields.

    # Methods - functions inside a class
    def saludar(self): 
        return f"Hola, soy {self.nombre} y tengo {self.edad} años." 

    def cumplir_años(self):
        self.edad += 1
        return f"{self.nombre} ahora tiene {self.edad} años."
    
    def _str_(self): # These are special methods, called
        return f"La persona de nombre {self.name} y edad{self.edad}"
    

# Create objects (instances of the class)
persona1 = Persona("Juan", 25)
persona2 = Persona("Ana", 30)

print(persona1.saludar())

print(persona1) # Displays an object in memory.

print(persona1) # It is necessary to define _str_ in the class, overloading the 'toString' method
