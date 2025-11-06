# 10. Club “Noche Estelar” — Acceso + validación documento

# Pedir edad y documento.

# Reglas:

#     Edad ≥ 18 → puede entrar solo si tiene documento.
#     Si la edad < 18 → "Entrada denegada"
    # Si tiene 18 o más pero no tiene documento → "Debe presentar documento"

# MY VERSION

age = int(input("HOw old are you?"))
document = input("What is your ID?")

def access(age, id):
    if(age >= 18 and id != ""):
        return "welcome"
    elif(age >=18):
        return "The document is neccesary please show it to the staff"
    else:
        return "Entry denied"
    
print(access(age,document))

# CHATGPT VERSION

# Ask for user input
age = int(input("How old are you? "))
document = input("What is your ID? ").strip()  # strip() removes accidental spaces

def access(age: int, document: str) -> str:
    """Check if the user can access based on age and document."""
    if age < 0:
        return "Invalid age entered."
    elif age >= 18 and document:
        return "Welcome!"
    elif age >= 18 and not document:
        return "The document is necessary. Please show it to the staff."
    else:
        return "Entry denied. You must be 18 or older."
    
print(access(age, document))

# SUMMARY OF IMPROVEMENTS

# | Problem                         | Fix                                     |
# | ------------------------------- | --------------------------------------- |
# | Used `id` (Python built-in)     | Changed to `document` to avoid conflict |
# | Didn’t handle empty spaces      | Added `.strip()` to clean user input    |
# | No validation for negative ages | Added explicit check for `< 0`          |
# | Verbose `id != ""`              | Simplified to `if document:`            |
# | Missing documentation           | Added a short docstring                 |
# | Inconsistent capitalization     | Fixed “HOw” → “How”                     |
