import random
import os

# Extra function: (To improve console readability).

def limpiar_consola():
    os.system('clear')


class Arma:

    # Initialize the weapon:
    def __init__(self, tipo, rareza):
        self.tipo = tipo
        self.rareza = rareza
        self.daño = self.definir_daño()

    # The weapon's damage is random:
    def definir_daño(self):
        if self.rareza == "Común":
            return random.randint(20, 40)
        elif self.rareza == "Rara":
            return random.randint(41, 70)
        elif self.rareza == "Legendaria":
            return random.randint(71, 100)

    # Present the weapon:
    def __str__(self):
        return f"{self.tipo} ({self.rareza}, damage: {self.daño})"


class Luchador:
     
    # The fighter's attributes are generated randomly
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = random.randint(100, 1000)
        self.critico_maximo = random.randint(10, 50)
        self.prob_esquive = round(random.uniform(0.1, 0.5), 2)
        self.arma = self.generar_arma()

    # The weapon is generated randomly.
    def generar_arma(self):
        tipos = ["Espada", "Hacha", "Lanza", "Ballesta"]
        rarezas = ["Común", "Rara", "Legendaria"]
        tipo = random.choice(tipos)
        rareza = random.choice(rarezas)
        return Arma(tipo, rareza)

    def esta_vivo(self):
        return self.vida > 0

    # Calculates the chance to dodge a given attack.
    def intentar_esquivar(self):
        return random.random() < self.prob_esquive

    def atacar(self, enemigo):

        # Calculates the chance to use the attacker's critical damage.
        critico_aleatorio = round(random.uniform(0, 1), 2)  # E.g.: 0.27
        daño_critico = round(self.critico_maximo * critico_aleatorio)

        # There is a possibility to dodge the attack.
        if enemigo.intentar_esquivar():
            return f"{enemigo.nombre} dodged {self.nombre}'s attack!"
        
        # Otherwise, the attack cannot be dodged.
        daño_total = 30 + self.arma.daño + daño_critico
        enemigo.vida -= daño_total

        # Correct in case the enemy's life becomes negative.
        enemigo.vida = max(0, enemigo.vida)

        return f"{self.nombre} attacked with their {self.arma.tipo} causing {daño_total} damage. Remaining life of {enemigo.nombre}: {enemigo.vida}"

    # Presents the generated fighter.
    def __str__(self):
        return f"{self.nombre} - Life: {self.vida}, Dodge: {self.prob_esquive}, Critical: {self.critico_maximo}, Weapon: {self.arma}"


    

# =============================================== #
# ================= BATTLE ====================== #
# =============================================== #


import random

print() # Clean up the terminal.

# Create two fighters
luchador1 = Luchador(input("Please enter the name of fighter 1: "))
luchador2 = Luchador(input("Please enter the name of fighter 2: "))

print() # Clean up the terminal.

# Show initial info
print("The battle begins!\n")
print(luchador1)
print(luchador2)
print()

# Randomly choose who starts
turno = random.choice([luchador1, luchador2])

# Battle
while luchador1.esta_vivo() and luchador2.esta_vivo():
    atacante = turno
    defensor = luchador1 if atacante is luchador2 else luchador2

    resultado = atacante.atacar(defensor)
    print(resultado)
    print()

    # Change turn
    turno = defensor

    # Interface during the game
    input("- Press Enter to continue to the next turn... ")
    limpiar_consola()
    print(luchador1)
    print(luchador2)
    print()


# Determine winner
ganador = luchador1 if luchador1.esta_vivo() else luchador2
print(f"{ganador.nombre} has won the battle!")
