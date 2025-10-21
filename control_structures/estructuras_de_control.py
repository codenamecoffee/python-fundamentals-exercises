edad = 18

if edad >= 18:
    print("You are an adult.")
elif edad >= 13:
    print("You are a teenager.")
else:
    print("You are a minor.")

# Comparison operators:
# == (equal)
# != (not equal)
# >, <, >=, <=

# Logical operators:
# and, or, not


print()
print('''=====================================================================''')
print()
 
 # The closest thing to 'Switch - Case' in Python (from version 3.10 onwards)
 # is 'match - case':


while True:
    print() # Line break for better visualization

    print("""
    Choose an option:
    1. Option 1
    2. Option 2
    3. Exit
    """)

    opcion = input("Chosen option: ") 
    
    # The indentation of the comment in the input is taken as indentation in the output.
    # Even line breaks, without needing to use escape sequences.
    
    # Therefore, this:

# 1. Option 1

   # Is not the same as this:

#     1. Option 1

   # It seems silly, but in the terminal the indentation of the comment is respected. (Interesting)

    match opcion:
        case "1":
            print("\n=> Option 1 selected")
        case "2":
            print("\n=> Option 2 selected")
        case "3":
            print("\nExiting...")
            break
        case _:
            print("\n=> Invalid option")


