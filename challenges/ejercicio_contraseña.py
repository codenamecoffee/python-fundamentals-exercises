def esContraseña_Segura(contraseña):
    
    if len(contraseña) < 8:
        print("\nThe password must have at least 8 characters.\n")
        return False
    
    mayuscula, minuscula, numero = False, False, False
    
    for char in contraseña:
        if char.isupper():
            mayuscula = True
        elif char.islower():
            minuscula = True
        elif char.isdigit():
            numero = True

    if not mayuscula:
        print(f"\nThe password must contain at least one uppercase letter.\n")
        return False
    if not minuscula:
        print(f"\nThe password must contain at least one lowercase letter.\n")
        return False
    if not numero:
        print(f"\nThe password must contain at least one number.\n")
        return False

    return True
    
while (not esContraseña_Segura(contraseña := input("Enter a secure password: "))):
    print(f"=> Insecure password. Please try again.\n")

print(f"\nSecure password entered:", contraseña)