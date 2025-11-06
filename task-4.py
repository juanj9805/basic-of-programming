# 4. Heladería “Frosty” — Sabor y topping

# Sabores y precios:

#     chocolate → $4.000
#     vainilla → $3.500

# Opcional: topping cuesta $1.000.

# Si el usuario ingresa un sabor que no existe, mostrar "Sabor no disponible".
# Si el sabor es válido, preguntar si quiere topping y calcular total.

# MY VERSION

iceCream = int(input("Choose one flavor: 1- for chocolate($4.000) or 2- for vanila($3.500)"))

def choice (option):
    if (option == 1):
        return "Your choice was chocolate and the Total amount is $4.000"
    elif (option == 2):
        return "Your choice was vanila and the Total amount is $3.500"
    elif (option == 3 ):
        return "DO you want a topping"
    else:
        return "Something went wrong"
    
print(choice(iceCream))

# CHATGPT VERSION

# Ask for flavor
flavor = input("Choose one flavor: chocolate ($4,000) or vanilla ($3,500): ").lower()

# Function to calculate total price
def calculate_price(flavor):
    """Return the total price based on flavor and optional topping."""
    # Define prices
    prices = {"chocolate": 4000, "vanilla": 3500}
    
    # Validate flavor
    if flavor not in prices:
        return "Flavor not available."
    
    # Ask about topping
    topping = input("Do you want a topping for an extra $1,000? (yes/no): ").lower()
    
    total = prices[flavor]
    
    if topping == "yes":
        total += 1000
    
    return f"Your choice was {flavor.capitalize()}, and your total is ${total:,}."

# Run the program
print(calculate_price(flavor))

# SUMMARY OF IMPROVEMENTS

# | Problem                            | Fix                                      |
# | ---------------------------------- | ---------------------------------------- |
# | Confusing numeric flavor selection | Ask for the flavor name directly         |
# | Useless `option == 3`              | Removed and replaced with topping prompt |
# | Repeated text                      | Used variables and dictionary mapping    |
# | Unclear error message              | Added `"Flavor not available"`           |
# | Grammar errors                     | Fixed for clarity and professionalism    |
# | Hard-to-scale structure            | Modularized with `prices` dictionary     |
