# While
print()

contador = 0

while contador < 3: 
    print(f"Counter: {contador}")
    contador += 1  # There is no contador++


print()
print('''=====================================================================''')
print()


# Repeat until the user enters what we want:

entrada = ""

while entrada != "salir":
    entrada = input("Type 'salir' to finish: ") # input() takes user data.

print("You exited the while loop.")


print()
print('''=====================================================================''')
print()


# Validate a password (simple):

while True:
    contraseña = input("Enter a password with at least 8 characters: ")
    if len(contraseña) >= 8:
        print("Password accepted!")
        break
    print("Too short, try again.")

# You can use 'while True', causing an infinite loop
# that is stopped with a 'break', instead of using boolean variables.

# [Warning]: without 'break', the loop never ends and the program hangs.
# Use 'ctrl + c' to interrupt execution in the terminal if needed.


print()
print('''=====================================================================''')
print()


# Avoid errors with validations:

numero = 0

while numero <= 0:
    try:
        numero = int(input("Enter a number greater than zero: "))
    except ValueError:
        print("That's not a number.")

# 'try - except' is similar to 'try - catch' in other languages.


print()
print('''=====================================================================''')
print()


# Useful keywords with while: 

# break: ends the loop or cycle.
# continue: ends the current iteration and jumps to the next. Does not end the loop.
# else: executes when the loop finishes, unless it was interrupted with a 'break'.


# Example with everything:

contador = 0

while contador < 100:
    try:
        numero = int(input("Enter a number to add to the counter: "))
        contador += numero
    except ValueError:
        print("That's not a number.")
        continue  # Jumps to the next iteration of the while.

    if numero <= 0:
        print("If we subtract or add 0, we'll never finish, bye.")
        break # Exits the while.
    
    print(f"The counter is now {contador}.")
else:
    print("You reached 100 or more!")


print()
print('''=====================================================================''')
print()


