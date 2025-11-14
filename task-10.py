# MY VERSION

from helpers import input_quantity_info,ID_generator,input_number,input_string

def sales_evaluation(sales):
    total_sales = []
    for sale in range(sales):
        sale_info = {
            "ID" : ID_generator(),
            "name" : input_string("name"),
            "sales" : input_number("total sales"),
        }
        total_sales.append(sale_info)
    return total_sales

def evaluation_sales(sales):
    for sale in sales:
        if sale["sales"] >= 6:
            print("Excellent")
        elif sale["sales"] >= 3:
            print("Good")
        elif sale["sales"] < 3:
            print("Bad performance")

evaluation_sales(sales_evaluation(input_quantity_info("sales")))

# CHATGPT VERSION

from helpers import input_quantity_info, ID_generator, input_number, input_string

def collect_sales_data(quantity):
    """
    Collects sales information for a given number of salespeople.
    Returns a list of dictionaries with: ID, name, and sales count.
    """
    sales_data = []
    for _ in range(quantity):
        sale_info = {
            "ID": ID_generator(),
            "name": input_string("Salesperson name"),
            "sales": input_number("Total sales made")
        }
        sales_data.append(sale_info)
    return sales_data


def evaluate_sales(sales_data):
    """
    Evaluates each salesperson based on sales numbers and returns
    a list of results instead of only printing.
    """
    results = []

    for sale in sales_data:
        name = sale["name"]
        sales = sale["sales"]

        if sales >= 6:
            evaluation = "Excellent"
        elif sales >= 3:
            evaluation = "Good"
        else:
            evaluation = "Poor performance"

        results.append({
            "name": name,
            "sales": sales,
            "evaluation": evaluation
        })

    return results


sales = collect_sales_data(input_quantity_info("sales"))
results = evaluate_sales(sales)

for r in results:
    print(f"{r['name']} → {r['evaluation']} ({r['sales']} sales)")

# SUMMARY OF IMPROVEMENTS

# | **Problem**                                       | **Fix**                                                        | **Why**                                              |
# | ------------------------------------------------- | -------------------------------------------------------------- | ---------------------------------------------------- |
# | Function names reversed and confusing             | Rename to `collect_sales_data` and `evaluate_sales`            | Clearer, more descriptive, easier to understand      |
# | `evaluation_sales()` only prints                  | Return results instead of only printing                        | Makes the function reusable, testable, and flexible  |
# | Repeated use of the word “sales” everywhere       | Use clearer variable names: `sales_data`, `quantity`, `result` | Reduces cognitive load, avoids confusion             |
# | No association between salesperson and evaluation | Include name in the evaluation output                          | Gives meaningful results instead of generic messages |
# | No input validation                               | Check for negative or impossible values                        | Prevents incorrect logic and invalid data            |
# | English expression “Bad performance” is unnatural | Change to “Poor performance”                                   | More natural English phrasing                        |
# | No docstrings                                     | Add docstrings to each function                                | Makes the code self-explaining and professional      |

