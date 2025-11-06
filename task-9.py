# 9. Supermercado “AhorroMax” — Descuentos y envío

# Cada producto cuesta $2.000.

# Reglas:

#         30 unidades → 15% descuento

#         10 unidades → 5% descuento

#     Si el total después del descuento es < $50.000 → agregar $5.000 de envío

# Calcular total final.

# MY VERSION

product_price = 2000
discount_15 = 0.15
discount_5 = 0.05
delivery_cost = 5000

def total_price (products_amount):
    total = products_amount * product_price
    if(products_amount >= 30):
        final_price = total - (total * discount_15)
        return final_price  
    elif(products_amount >= 10):
        final_price = total - (total *discount_5)
        return final_price  
    else:
        return "Something went wrong"

total = total_price(22)

def delivery_fee (total):
    if(total < 50000):
        delivery_total = total + delivery_cost
        return delivery_total

print(delivery_fee(total))

# CHATGPT VERSION

# Constants (always define fixed values in uppercase)
PRODUCT_PRICE = 2000
DISCOUNT_15 = 0.15
DISCOUNT_5 = 0.05
DELIVERY_COST = 5000

def total_price(products_amount: int) -> float:
    """Calculate total price applying discounts based on product amount."""
    if products_amount < 0:
        return "Error: Product amount cannot be negative."
    elif products_amount == 0:
        return 0

    total = products_amount * PRODUCT_PRICE

    if products_amount >= 30:
        final_price = total * (1 - DISCOUNT_15)
    elif products_amount >= 10:
        final_price = total * (1 - DISCOUNT_5)
    else:
        final_price = total  # No discount for fewer than 10 products

    return final_price

def delivery_fee(total: float) -> float:
    """Add delivery cost if the total is below 50,000."""
    if isinstance(total, str):
        return total  # Handle errors passed from total_price()
    if total < 50000:
        return total + DELIVERY_COST
    return total  # No fee if over threshold

# Example usage
total = total_price(22)
print(f"Subtotal: ${total:,.0f}")
print(f"Final total (with delivery if applies): ${delivery_fee(total):,.0f}")


# SUMMARY OF IMPROVEMENTS

# | Problem                              | Fix                                                                       |
# | ------------------------------------ | ------------------------------------------------------------------------- |
# | **Lowercase constants**              | Changed to uppercase (`PRODUCT_PRICE`, `DELIVERY_COST`, etc.) for clarity |
# | **Unclear return messages**          | Added descriptive error handling for invalid or zero amounts              |
# | **Repeated subtraction logic**       | Replaced with cleaner expression: `total * (1 - DISCOUNT)`                |
# | **No handling for small orders**     | Added fallback for orders with fewer than 10 products                     |
# | **Possible string arithmetic error** | Checked type with `isinstance(total, str)` in `delivery_fee()`            |
# | **Missing docstrings and typing**    | Added both to improve readability and IDE suggestions                     |
# | **No print formatting**              | Used `f"${total:,.0f}"` for user-friendly money display                   |
