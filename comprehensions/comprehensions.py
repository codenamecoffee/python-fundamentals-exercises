# What is a comprehension?

# A comprehension is a concise and expressive way to build 
# collections from iterations (like for loops) and conditions (if), 
# all in a single line. 



# ================================= #
####### LIST comprehension ##########
# ================================= #

## List comprehension || Syntax: [x for x in iterable] || Result: list

## Uses SQUARE brackets - pay attention

cuadrados = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
pares = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# In 'cuadrados', x**2 is the operation performed on each x in the iteration.
# In 'pares', it's like: for each x in the range, only take it if it's even (if)



# ================================= #
######## SET comprehension ##########
# ================================= #

# Set comprehension || Syntax: {x for x in iterable} || Result: set
## Uses curly braces - pay attention

cuadrados = {x**2 for x in [1, 2, 2, 3]}  # {1, 4, 9}

# When building the set, it ensures elements are not repeated.




# ================================= #
######## DICT comprehension #########
# ================================= #

# Dict comprehension || Syntax: {k: v for ...} || Result: dict
# Uses curly braces but with a key : value variable

numeros = [1, 2, 3]

cuadrados = {x: x**2 for x in numeros}  # {1: 1, 2: 4, 3: 9}

# x: x**2 => represents how we want the 'key:value' pair in the result




# ================================= #
####### Generator expression ########
# ================================= #

# Generator expression || Syntax: (x for x in iterable) || Result: generator
# Similar to list comprehension, but returns a generator, which is evaluated lazily:

gen = (x**2 for x in range(3))  # Not a list, but a generator

for valor in gen:
    print(valor)
# Output: 0 1 4

# Ideal for large volumes of data, since it doesn't store the whole collection in memory, but generates 
# the elements one by one as needed.




## How do they differ from "normal" collections?

# - Normal:

# Uses for loops, append(), etc.
# More code, less readable


# - Comprehension:

# Uses a single compact line
# Cleaner and more expressive code


# Example: Normal vs Comprehension

# Normal
resultado = []
for x in range(10):
    if x % 2 == 0:
        resultado.append(x * 2)

# Comprehension
resultado = [x * 2 for x in range(10) if x % 2 == 0]





# What are they for?

# To easily transform data.

# To filter elements.

# To efficiently build complex structures.

# To write cleaner code, especially in scripts or notebooks.