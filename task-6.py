# 6. Parqueadero “RapidCar” — Tarifa escalonada

# Tarifa:

#     0 a 5 horas: $2.000 x hora

#         5 horas: $2.000 x hora + multa fija de $5.000

# Validar horas:

#     No permitir números negativos.

# Mostrar valor total.

# MY VERSION

penaltyFee = 5000
pricePerHours = 2000
hours = int(input("How many hours are?"))

def parkingPrice (hours):
    if(hours<=0):
        return "Something went wrong"
    elif(hours>0 and hours <=5):
        return f"Total amount is {pricePerHours*hours}"
    elif(hours>5):
        return f"total amount is {(pricePerHours*hours)+penaltyFee}"
    else:
        return "Strings aren't allowed"

print(parkingPrice(hours))

# CHATGPT VERSION

penalty_fee = 5000
price_per_hour = 2000

def parking_price(hours):
    """Calculate total parking price based on time."""
    if hours < 0:
        return None  # Invalid
    elif hours < 5:
        return price_per_hour * hours
    elif hours == 5:
        return (price_per_hour * hours) + penalty_fee
    else:  # hours > 5
        return (price_per_hour * hours) + penalty_fee

# Ask user input
hours = int(input("How many hours did you park? "))

total = parking_price(hours)

if total is None:
    print("Invalid number of hours.")
else:
    print(f"Total amount to pay: ${total:,.0f}")

# SUMMARY OF IMPROVEMENTS

# | Problem                 | Fix                                    |
# | ----------------------- | -------------------------------------- |
# | Wrong invalid condition | Changed `<= 0` → `< 0`                 |
# | Missed 5-hour penalty   | Added exact check for 5 hours          |
# | Redundant condition     | Simplified logic                       |
# | Mixed logic & UI        | Separated logic from output            |
# | Naming                  | Used Pythonic snake_case               |
# | Unclear error message   | Added specific, user-friendly feedback |
