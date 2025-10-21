import random

print()
print("=> Random little game:")
print()

numero_secreto = random.randint(1, 10)
numero_elegido = None
intentos = 0

print(f"(If you want to cheat: (it's {numero_secreto})")

print("Guess the number between 1 and 10!\n") 

while True:
   
   # Update the number of attempts
   intentos += 1

   numero_elegido = int(input("Your number: "))
   if numero_elegido == numero_secreto:
      print(f"Correct! The number was {numero_secreto}.\n")

      # In honor of the true ternary operator:
      # (condition) ? value1 : value2 

      # Ternary operator involved to complete the word attempt or attempts
      print(f"You guessed it in {intentos} attempt{'s' if intentos > 1 else ''}.")
      break