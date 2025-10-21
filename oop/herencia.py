# Parent Class (Base)

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre 

    def hacer_sonido(self):
        return f"{self.nombre} hace un sonido."
    
    def dormir(self):
        return f"{self.nombre} está durmiendo."
    

# Child Classes (Inherit from 'Animal' class)

# Inheritance is passed as a parameter to the class...

class Perro(Animal):
    def hacer_sonido(self):  # Overrides the method (just like that - interesting)
        return f"{self.nombre} dice: ¡Guau!"
    
    def traer_pelota(self):
        return f"{self.nombre} trae la pelota."
    
class Gato(Animal):
    def hacer_sonido(self):
        return f"{self.nombre} dice: ¡Miau!"
    
    def ronronear(self):
        return f"{self.nombre} está ronroneando."
    

# Instantiate child classes (subclasses of 'Animal' class)
mi_perro = Perro("Max")
mi_gato = Gato("Luna")

print(mi_perro.hacer_sonido())
print(mi_gato.dormir())