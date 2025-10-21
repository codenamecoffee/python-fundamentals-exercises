# ========================================================== #
##################### Tuples (tuple) #########################
# ========================================================== #

# Ordered
# Allow duplicates
# Immutable (Cannot be modified)
# Indexed just like lists.

coordenadas = (10, 20)
print(coordenadas[0]) # Access by index

# Although they are immutable, they can contain mutable objects inside (like lists),
# and those can be modified.

mi_tupla = ([1, 2], 3)
mi_tupla[0].append(4)   # This works, because the content is a list (mutable)


print("=======================================================")
print("=======================================================")
print("=======================================================")

# Operations on tuples:

# Indexing
t = (1, 2, 3)
print(t[0])  # 1


# Slicing
print(t[1:])  # Output: (2, 3) - From position '1' to the end.


# Concatenation
nueva = t + (4, 5)
print(f"New tuple: {nueva}")


# Repetition 
repetida = t * 2  # Output (1, 2, 3, 1, 2, 3) - Stores 't' concatenated twice.


# ========================================================== #
################### Strings (str) ###########################
# ========================================================== #

# Ordered
# Indexable
# Immutable

mensaje = "hola"


print("=======================================================")
print("=======================================================")
print("=======================================================")

# Operations on str:

# Indexing
s = "python"
print(s[0])    # 'p'


# Slicing
print(s[1:4])  # 'yth' 

# => Shows from index 1(y) to 4 without including it, so 3(h)


# Concatenation
nuevo = s + "3"  # 'python3'


# Repetition
print("ha" * 3)  # 'hahaha'


# Common methods that return a new string:
a_mayusculas = s.upper()
a_minusculas = s.lower() 
remplaza_p_por_b = s.replace("p", "b")
separa_caracteres_segun_t= s.split("t")

no_whitespace = s.strip() # Removes whitespace at the beginning and end


# ========================================================== #
####################### frozenset (str) ######################
# ========================================================== #

# Being immutable, it cannot be changed, but you can perform
# set operations (they return new sets):

a = frozenset([1, 2, 3])
b = frozenset([2, 3, 4])

a.union(b)        # frozenset({1, 2, 3, 4})
a.intersection(b) # frozenset({2, 3})
a.difference(b)   # frozenset({1})
a.issubset(b)     # False
