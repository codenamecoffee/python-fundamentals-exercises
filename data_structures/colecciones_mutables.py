# ========================================================== #
######################## LISTS ###############################
# ========================================================== #

# Of the same type
frutas = ["manzana", "banana", "naranja"] 
numeros = [1, 2, 3, 4, 5]

# Of different types (Shows it's not an array)
mixta = [1, "manzana", True, 1.34, { "clave" : "café"}, ['otra', 'lista']]

# Access elements using the index, like arrays:

# mixta[0]
# Can be modified: mixta[0] = 20
# Can even change type: mixta[0] = False 

# Likewise:
# - With normal variables you can also change type as above.  


""" ==================================================== """
""" ==================================================== """
""" ==================================================== """

print()

# Operations on lists #

frutas.append("uva")

# See the changes
print(f"'uva' was added to the end: {frutas}")

frutas.insert(0, "mango")

# See the changes
print(f"'mango' was added to the beginning: {frutas}")

frutas.remove("manzana")

# See the changes
print(f"'manzana' was removed: {frutas}")

fruta_eliminada = frutas.pop()  # Remove and return last

print(f"About to remove the last element: {fruta_eliminada}")

print(f"The last element was removed: {frutas}")


# ========================================================== #
#################### DICTIONARIES (dict) #####################
# ========================================================== #


print() # Tidying up the output.

# Preserve insertion order
# Use unique keys
# Used to represent objects and structured data.

persona = {
    "nombre": "Ana", 
    "edad": 30
}

print(f"Dictionary \"persona\" = {persona}")

persona["edad"] = 31              # Modify

persona["ciudad"] = "Montevideo"  # Add new key

del persona["nombre"]             # Delete key

print(f"Persona after operations: {persona}")


""" ==================================================== """
""" ==================================================== """
""" ==================================================== """

# Operations on Dictionaries #

persona.keys()     # Returns the keys

print(f"The keys of the persona object are: {persona.keys()}")

persona.values()   # Returns the values

print(f"The values of the persona object are: {persona.values()}")

persona.items()    # Returns pairs (key, value)

print(f"The key-value pairs of the persona object are: {persona.items()}")


# ========================================================== #
###################### Sets (set) ###########################
# ========================================================== #

print()
# Unordered 
# Do not allow duplicate elements 
# Ideal for set theory operations (union, intersection, difference, ...)

colores = {"rojo", "azul"}
print(colores)

colores.add("verde")         # Add elements
print(f"The color verde was added: {colores}")

colores.remove("azul")       # Remove elements
print(f"The color azul was removed: {colores}")

# Note: There is also 'frozenset' which is immutable, but set is mutable.

""" ==================================================== """
""" ==================================================== """
""" ==================================================== """


# Operations on sets

# Example sets:

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # Union
print(a & b)   # Intersection
print(a - b)   # Difference


