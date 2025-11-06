# 2. Cine “La Estrella” — Tarifas por edad

# Pedir la edad del cliente:
# Edad 	Precio
# < 5 años 	Entrada gratis
# 5 a 11 	$5.000
# 12 a 59 	$8.000
# ≥ 60 	$4.000 (descuento adulto mayor)

# Mostrar el precio.
# Si la edad es negativa, mostrar error.

# MY VERSION

age = int(input("How old are you: "))

def fare (age):
    if(age<0):
        return "Invalid age"
    elif age < 5:
        return "Join free"
    elif age >= 5 and age <=11:
        return "$5.000"
    elif age >= 12 and age <=59:
        return "$8.000"
    elif age >= 60:
        return "Eldery discount $4.000"
    else:
        return "Something went wrong"
    
print(fare(age))


# CHATGPT VERSION

def get_ticket_price(age):
    """Return the ticket price based on the customer's age."""
    if age < 0:
        return None  # invalid input
    elif age < 5:
        return 0
    elif age <= 11:
        return 5000
    elif age <= 59:
        return 8000
    else:
        return 4000

age = int(input("How old are you: "))
price = get_ticket_price(age)

if price is None:
    print("Invalid age entered.")
elif price == 0:
    print("Free entry!")
else:
    print(f"Your ticket price is ${price:,}")

# SUMMARY OF IMPROVEMENTS

# | Problem                | Fix                                 |
# | ---------------------- | ----------------------------------- |
# | No negative validation | Added explicit check                |
# | Repeated conditions    | Simplified ranges                   |
# | Mixed return types     | Returned consistent numeric data    |
# | Confusing messages     | Separated logic from UI             |
# | Naming                 | More descriptive, professional name |
