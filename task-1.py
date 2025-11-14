# MY VERSION
from helpers import input_quantity_info, ID_generator, input_string, input_number

products = []

def products_register(quantity):
    for product in range(quantity):
        expired =  input(f"Product {product+1} is expired?: ")

        product_info =  {
            "ID" : ID_generator(),
            "name": input_string("Product name"),
            "quantity": input_number("Quantity"),
            "price": input_number("price"),
            "expired": expired,
        }
        products.append(product_info)

products_register(input_quantity_info("products"))

# Total 

# CHATGPT VERSION

# def products_register(quantity):
#     products = []
#     for i in range(quantity):
#         try:
#             name = input(f"Product {i + 1} name: ")
#             product_quantity = int(input("Product quantity: "))
#             price = int(input("Product price: "))
#             expired = input("Is it expired? (yes/no): ")

#             product_info = {
#                 "name": name,
#                 "quantity": product_quantity,
#                 "price": price,
#                 "expired": expired.lower()
#             }

#             products.append(product_info)

#         except ValueError:
#             print("Please enter valid numbers for quantity and price.")

#     return products


# products_quantity = int(input("How many products do you want to register: "))
# products = products_register(products_quantity)

# print("\nRegistered products:")
# print(products)


# print(products_register())


# # SUMMMARY OF IMPROVEMENTS

# # | **Problem**                                                 | **Fix**                                                                     | **Why**                                                                                  |
# # | ----------------------------------------------------------- | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
# # | The function **doesn’t return anything**                    | Add `return products` at the end of the function                            | Without a `return`, `print(products_register(...))` prints `None`                        |
# # | You’re using the global list `products` inside the function | Create a **local list** inside the function (`products = []`) and return it | Avoids side effects and makes the function reusable                                      |
# # | You’re printing `products` **inside the loop**              | Move the `print(products)` line **after** the loop, or remove it            | Printing in every iteration can clutter the console and isn’t necessary for final output |
# # | Variable name `quantity` is reused inside the loop          | Rename the inner variable to `product_quantity`                             | Avoids overwriting the function parameter and prevents confusion                         |
# # | No input validation or error handling                       | Wrap conversions (`int(input(...))`) in a `try/except ValueError`           | Prevents program crashes if the user types non-numeric input                             |
# # | Global variable `products_quantity` is defined outside      | Pass it directly as a parameter to keep function independent                | Increases flexibility and reduces reliance on global state                               |
