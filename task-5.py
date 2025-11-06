# 5. Librería “El Saber” — Descuento estudiante + cupón

# Libro cuesta $25.000.

#     Si es estudiante → 15% descuento
#     Si además tiene cupón "LIBRO10" → 10% adicional sobre el valor ya descontado

# Validar:

#     Si no es estudiante, el cupón no aplica.
#     Si ingresa cupón incorrecto, ignorarlo.

# Mostrar total.

# MY VERSION

bookPrice = 25.000
coupon = "LIBRO10"
person = "student"

def totalBook (who, discount ="none"):
    if(who != "student"):
        return f"total amount {bookPrice}"
    elif(who != "student" and discount == coupon):
        return f"Total amount{bookPrice * 0.9}"
    elif(who == "student" and discount == coupon):
        return f"total amount {bookPrice*0.75}"
    elif(who == "student"):
        return f"total amount {bookPrice*0.85}"
    else:
        return"Something went wrong"


print(totalBook(person,coupon))


# CHATGPT VERSION

book_price = 25000
valid_coupon = "LIBRO10"

def total_book(person_type, coupon_code=None):
    """Calculate the total book price with discounts."""
    
    # If not a student → no discounts apply
    if person_type != "student":
        return book_price
    
    # If student and has valid coupon → 15% + 10% (on already discounted)
    if coupon_code == valid_coupon:
        total = book_price * 0.85 * 0.9
        return total
    
    # If student without coupon → only 15% discount
    return book_price * 0.85

# Example test
total = total_book("student", "LIBRO10")
print(f"The total amount to pay is: ${total:,.0f}")


# SUMMARY OF IMPROVEMENTS

# | Problem                     | Fix                                  |
# | --------------------------- | ------------------------------------ |
# | Wrong price (25.000 → 25.0) | Fixed to 25000                       |
# | Unreachable condition       | Reordered condition checks           |
# | Wrong discount math         | Applied correct compound discount    |
# | Mixed logic + UI            | Returned data only                   |
# | Naming style                | Used Pythonic snake_case             |
# | Clarity                     | Added docstring and formatted output |
