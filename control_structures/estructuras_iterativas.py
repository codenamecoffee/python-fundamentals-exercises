# For with range() - For numeric purposes

# => range(5) generates a sequence from 0 to 4 (does not include the last).

for i in range(5):
    print(f"Number: {i}")

print()
# Range with parameters. (Does not include the last number)

for i in range(1, 6):  # from 1 to 5 - Does not include 6
    print(i)

print()
# By 2s thanks to the third parameter

for i in range(0, 10, 2):  # from 0 to 8, by 2 - Does not include 10
    print(i)

print()
# To go backwards, use range() in reverse, with a negative step:

for i in range(5, 0, -1):  # from 5 to 1 - Does not include 0
    print(f"Number: {i}")

print()
print('''=====================================================================''')
print()


# For with lists (They have the versatility of an array, but are not arrays)

frutas = ["manzana", "banana", "naranja", "kiwi"] 

for fruta in frutas:
    print(f"Fruit: {fruta}") 


print()
print('''=====================================================================''')
print()


# For over a string
palabra = "python"

for letra in palabra:
    print(letra)

print()
# If we want to show everything on the same line:
for letra in palabra:
    print(letra, end="|") # 'end' avoids the line break, and "|" is added between each letter.

print()


print()
print('''=====================================================================''')
print()


# For over a dictionary (dict)

persona = {
    "nombre": "Ana", 
    "edad": 30
}

for clave in persona:
    print(clave, "→", persona[clave])


print()
# or directly: (declaring more control variables + items().)
for clave, valor in persona.items():
    print(clave, "→", valor)


print()
print('''=====================================================================''')
print()


# Enumerate a list with enumerate()

frutas = ["manzana", "naranja", "banana"]

for i, fruta in enumerate(frutas):  # Similar to 'items()' with dictionaries.
    print(f"{i}: {fruta}")


print()
print('''=====================================================================''')
print()


# Iterate over multiple lists at once with zip()

nombres = ["Ana", "Luis", "Pedro"]
edades = [30, 25, 40]
profesiones = ["Ingeniera", "Médico", "Abogado"]

for nombre, edad, profesion in zip(nombres, edades, profesiones):
    print(f"{nombre} | {profesion}: is {edad} years old.")


