import time

# 1. Panadería de Don Pancho — Descuentos por cantidades

# La panadería de Don Pancho vende pan a $300 cada uno.

# Reglas:

#     Si compra más de 20 panes → 10% descuento
#     Si compra más de 50 panes → 20% descuento
#     Si ingresa una cantidad negativa, mostrar "Cantidad inválida"

# Calcular y mostrar el total.

# MY VERSION

sales = {}

priceBread = 300

def totalBreads (amount,priceBread):

    if amount <=0:
        return "Something went wrong"
    elif amount>20 and amount<50:
        total = (amount*priceBread)*0.9
        return total
    elif amount>50:
        total = (amount*priceBread)*0.8
        return total
    else:
        total = amount*priceBread
        return total

# Id generator 

def random_id_generator ():
    return str(int(time.time()))

sales[random_id_generator()] = totalBreads(21,priceBread)

print(sales)


# CHATGPT VERSION

priceBread = 300

def totalBreads(amount, priceBread):
    if amount <= 0:
        return "Cantidad inválida"
    elif amount > 50:
        total = amount * priceBread * 0.8
    elif amount > 20:
        total = amount * priceBread * 0.9
    else:
        total = amount * priceBread
    return f"Total a pagar: ${total:,.0f}"

# print(totalBreads(0, priceBread))



# SUMMARY OF IMPROVEMENTS

# | Aspect                | Your version                     | Improved version               |
# | --------------------- | -------------------------------- | ------------------------------ |
# | Handles all cases     | Missing 1–20 range               | Covers all cases           |
# | Error message         | “Something went wrong” (generic) | “Cantidad inválida” (specific) |
# | Condition readability | Redundant `> 20 and < 50`        | Simpler, ordered logic         |
# | Output formatting     | Plain number                     | Formatted as money             |
# | Return value safety   | Can return `None`                | Always returns a string        |
