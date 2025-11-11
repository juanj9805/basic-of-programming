# 🛒 Exercise: Tech Store — Manage Your Shopping Cart
# 🎯 Goal

# Create a program that manages a small online tech store.
# You'll use a dictionary to store product information and simulate a shopping experience.

# 🧩 Requirements

# Create a dictionary called products with at least 4 items, using this format:

# products = {
#     101: {"name": "Mouse", "price": 20000},
#     102: {"name": "Keyboard", "price": 45000},
#     103: {"name": "Headphones", "price": 60000},
#     104: {"name": "Monitor", "price": 300000},
# }


# Ask the user to enter a product ID and quantity.

# Create a function called calculate_total(product_id, quantity) that:

# Looks up the product in the dictionary.

# Calculates the total cost (price × quantity).

# Returns a new dictionary containing:

# {"quantity": quantity, "total": total_price}


# Add a 10% discount if the total is over $2000

# Show the purchase summary like this:

# Quantity: 2
# Subtotal: $600,000
# Discount: $60,000
# Final Total: $540,000

# MY VERSION 

products = {
101: {"product":"Mouse", "price": 200},
102: {"product":"Keyboard", "price": 300},
103: {"product":"Headphones", "price": 500},
104: {"product":"Monitor", "price": 1500},
}
  
def calculate_total ():
    try:
        id = int(input("What is the code of the product: "))
        quantity = int(input("What is the quantity: "))
        total_price = products[id]["price"] * quantity
        name = products[id]["product"]
        return  (id,quantity,total_price,name)
    except KeyError:
        print("Product id dosen't exists")
    except ValueError:
        print("Please enter a valid number")


# print(calculate_total())

ADD_DISCOUNT = 0.1

def add_discount (discount):
    try:
        data = calculate_total()
        id = data[0]
        quantity = data[1]
        price = data[2]
        name = data[3]
        price_discount =  price * (1 - discount)
        return f"Product: {name}\nQuantity: {quantity}\nFinal total: {price_discount if price>600 else price}\nFull price is {price}"
    finally:
        print("Transaction succed")

# print(add_discount(ADD_DISCOUNT))

# CHATGPT VERSION

products = {
    101: {"product": "Mouse", "price": 200},
    102: {"product": "Keyboard", "price": 300},
    103: {"product": "Headphones", "price": 500},
    104: {"product": "Monitor", "price": 1500},
}

ADD_DISCOUNT = 0.10

def calculate_total():
    try:
        product_id = int(input("Enter product code: "))
        quantity = int(input("Enter quantity: "))
        product = products[product_id]
        total_price = product["price"] * quantity
        return {"id": product_id, "quantity": quantity, "price": total_price, "name": product["product"]}
    except KeyError:
        print("❌ Product ID doesn't exist.")
    except ValueError:
        print("❌ Please enter valid numbers.")
    return None

def add_discount(discount):
    data = calculate_total()
    if not data:
        return "⚠️ Transaction failed."
    
    price = data["price"]
    name = data["name"]
    quantity = data["quantity"]

    if price > 2000:
        discount_amount = price * discount
        final_price = price - discount_amount
    else:
        discount_amount = 0
        final_price = price

    return (
        f"Product: {name}\n"
        f"Quantity: {quantity}\n"
        f"Subtotal: ${price:,.0f}\n"
        f"Discount: ${discount_amount:,.0f}\n"
        f"Final Total: ${final_price:,.0f}\n"
        "✅ Transaction successful!"
    )

# print(add_discount(ADD_DISCOUNT))

# SUMMARY OF IMPROVEMENTS

# | Problem                          | Fix                              | Why                               |
# | -------------------------------- | -------------------------------- | --------------------------------- |
# | Used `finally` incorrectly       | Moved success message outside    | Prevents false “success” messages |
# | Used tuple instead of dictionary | Returned dictionary              | Improves readability              |
# | Output unclear                   | Added formatted multiline output | Makes summary user-friendly       |
# | No return on exception           | Added `return None`              | Prevents crashes                  |




