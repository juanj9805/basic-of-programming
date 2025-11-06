# 7. Restaurante “El Sabor Colombiano” — Menú + bebida opcional + IVA

# Menú: $12.000

# Opciones bebida:

#     sí → $3.000
#     no → $0

# Luego aplicar IVA del 8% al total final.
# Mostrar valor con IVA incluido.

# MY VERSION

menu_price = 12000
beverage = int(input("Drink options: 1- si($3.000) 2- no($0)"))

def totalMenu(dish,drink):
    """" Calculate total prices based on menu and beverages """
    if(drink == 1): 
        total = dish+3000 
        return f"Menu: ${dish:,}\nDrink: $3,000\nTotal: ${total:,}" 
    elif(drink ==2):
        total = dish * 0.8
        return f"Menu: ${dish:,.0f}\nDrink: $0\nTotal: ${total:,.0f}" 
    else:
        return "Something went wrong"

# Way to add thousand separator

# Easier 
# ${dish:,}

# Let us to add decimals 0f = without decimals, (n)f = n decimals 
# ${dish:,.0f}

print(totalMenu(menu_price, beverage))

# CHATGPT VERSION

MENU_PRICE = 12000
BEVERAGE_PRICE = 3000
IVA_RATE = 0.08

def totalMenu(dish, drink):
    """Calculate total price with optional beverage and 8% IVA"""
    if drink == 1:
        subtotal = dish + BEVERAGE_PRICE
        drink_label = "$3,000"
    elif drink == 2:
        subtotal = dish
        drink_label = "$0"
    else:
        return "❌ Invalid option. Please choose 1 (yes) or 2 (no)."

    total_with_iva = subtotal * (1 + IVA_RATE)

    return (
        f"Menu: ${dish:,.0f}\n"
        f"Drink: {drink_label}\n"
        f"Subtotal: ${subtotal:,.0f}\n"
        f"IVA (8%): ${(subtotal * IVA_RATE):,.0f}\n"
        f"Total: ${total_with_iva:,.0f}"
    )


try:
    beverage = int(input("Drink options: 1- yes ($3,000) or 2- no ($0): "))
    print(totalMenu(MENU_PRICE, beverage))
except ValueError:
    print("⚠️ Please enter a valid number (1 or 2).")



# SUMMARY OF IMPROVEMENTS

# | Problem                 | Fix                                    |
# | ----------------------- | -------------------------------------- |
# | Wrong invalid condition | Changed `<= 0` → `< 0`                 |
# | Missed 5-hour penalty   | Added exact check for 5 hours          |
# | Redundant condition     | Simplified logic                       |
# | Mixed logic & UI        | Separated logic from output            |
# | Naming                  | Used Pythonic snake_case               |
# | Unclear error message   | Added specific, user-friendly feedback |
