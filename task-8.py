# MY VERSION
from helpers import input_quantity_info,ID_generator,input_string,input_number

def bills_register(quantity):
    bills = []
    for i in range(quantity):
        bill_info = {
            "ID": ID_generator(),
            "name": input_string("name"),
            "amount": input_number("total amount"),
            "type": input_string("type: normal/premium")
        }
        bills.append(bill_info)
    print(bills)
    return bills

# bills_register(input_quantity_info("bills"))

def total_bills(bills):
    normal_discount = 0.05
    premium_discount = 0.1
    total = 0
    for bill in bills:
        if bill["type"] == "normal":
            total += bill["amount"] - (bill["amount"] * normal_discount)
        elif bill["type"] == "premium":
            total += bill["amount"] - (bill["amount"] * premium_discount)
        else:
            "Invalid bill type"
    return total

print(total_bills(bills_register(input_quantity_info("bills"))))

# CHATGPT VERSION

from helpers import input_quantity_info, ID_generator, input_string, input_number

def register_bills(quantity):
    bills = []
    for _ in range(quantity):
        bill_info = {
            "ID": ID_generator(),
            "name": input_string("name"),
            "amount": input_number("total amount"),
            "type": input_string("type: normal/premium")
        }
        bills.append(bill_info)
    return bills

def calculate_total_bills(bills):
    discounts = {
        "normal": 0.05,
        "premium": 0.10
    }

    total = 0

    for bill in bills:
        bill_type = bill["type"]
        if bill_type not in discounts:
            raise ValueError(f"Invalid bill type: {bill_type}")

        discount = discounts[bill_type]
        total += bill["amount"] * (1 - discount)

    return total

# bills = register_bills(input_quantity_info("bills"))
# print(calculate_total_bills(bills))

# SUMMARY OF IMPROVEMENTS

# | **Problem**                                               | **Fix**                                                                    | **Why**                                                                                             |
# | --------------------------------------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
# | `print(bills)` inside `bills_register()` mixes logic      | Remove print from inside the function and print only outside               | Keeps data logic separated from UI/output. Makes the function reusable and clean.                   |
# | `else: "Something went wrong"` does nothing               | Replace with `print()` or `raise ValueError()`                             | A string alone is ignored in Python. You need a real action to notify the error.                    |
# | Duplicate discount calculation logic                      | Use a discount dictionary and single expression: `amount * (1 - discount)` | Avoids repeated code (DRY principle). Makes it easier to modify discounts later.                    |
# | No validation for bill type                               | Add a check: `if bill_type not in discounts: raise ValueError(...)`        | Prevents invalid input from silently breaking the logic. Makes the code safer and more predictable. |
# | `bills_register` name reversed                            | Rename to `register_bills()`                                               | Verb-first naming is clearer and follows Python naming conventions.                                 |
# | `total_bills` name unclear                                | Rename to `calculate_total_bills()`                                        | Describes exactly what the function does, improving readability.                                    |
# | No docstrings explaining the function                     | Add docstrings describing behavior and discount rules                      | Helps future readers (including you) understand what the function expects and returns.              |
# | Premium discount > normal discount (may be unintentional) | Confirm the rule or swap values if needed                                  | Prevents logic errors caused by misunderstanding the business rules.                                |
# | No input validation for type field                        | Enforce valid input at the moment of entry (`normal/premium`)              | Prevents garbage data early and avoids errors later.                                                |
# | Unnecessary variable `for i in range(quantity)`           | Use `_` since the variable is unused                                       | Makes it clear that the loop index is irrelevant and avoids confusion.                              |
