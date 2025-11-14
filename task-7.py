# MY VERSION

import time

quantity_packages = int(input("How many packages do you want to store?: "))

def assign_type(packages):
    normal_list = []
    express_list = []
    urgent_list = []
    for package in range(packages):
        package_type = input(f"Put the type of the package:\n" 
        "-normal\n" 
        "-express\n" 
        f"-urgent\n{"-"*30}\n" 
        ).lower()
        print("-"*30)
        if package_type != "":
            if package_type == "normal":
                package_ID = time.time()
                package_name = input("Enter the name of the package: ")
                package_kind = package_type
                package_info = {
                    "package_ID": package_ID,
                    "package_name": package_name,
                    "package_kind": package_kind,
                }
                normal_list.append(package_info)
            elif package_type == "express":
                package_ID = time.time()
                package_name = input("Enter the name of the package: ")
                package_kind = package_type
                package_info = {
                    "package_ID": package_ID,
                    "package_name": package_name,
                    "package_kind": package_kind,
                }
                express_list.append(package_info)
            elif package_type == "urgent":
                package_ID = time.time()
                package_name = input("Enter the name of the package: ")
                package_kind = package_type
                package_info = {
                    "package_ID": package_ID,
                    "package_name": package_name,
                    "package_kind": package_kind,
                }
                urgent_list.append(package_info)
    return [normal_list,express_list,urgent_list]

print(assign_type(quantity_packages))

def packages_count_type(packages_type):
    packages_info = []
    for package in packages_type:
        package_amount = len(package)
        packages_info.append(package_amount)
    return packages_info


print(packages_count_type(assign_type(quantity_packages)))

# CHATGPT VERSION

import time

quantity_packages = int(input("How many packages do you want to store?: "))

def create_package(package_type):
    return {
        "package_ID": time.time(),
        "package_name": input("Enter the name of the package: "),
        "package_kind": package_type
    }

def assign_type(quantity):
    packages = {"normal": [], "express": [], "urgent": []}

    for _ in range(quantity):
        print("-" * 30)
        package_type = input(
            "Choose the type:\n"
            "- normal\n"
            "- express\n"
            "- urgent\n"
        ).lower()

        if package_type in packages:
            package_info = create_package(package_type)
            packages[package_type].append(package_info)
        else:
            print("❌ Invalid type. Package skipped.")

    return packages


def count_packages_by_type(data):
    return {category: len(items) for category, items in data.items()}


package_data = assign_type(quantity_packages)

print(package_data)
print(count_packages_by_type(package_data))

# SUMMARY OF IMPROVEMENTS 

# | **Problem**                                                 | **Fix**                                                                      | **Why**                                                           |
# | ----------------------------------------------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------------------------- |
# | Calling `assign_type()` twice                               | Call it once, store result in a variable                                     | Avoids duplicate user input and redundant work                    |
# | Invalid f-string inside input prompt                        | Remove nested `{}` or build prompt as a separate string                      | Prevents syntax errors and improves readability                   |
# | Repeated code for normal/express/urgent                     | Create a helper function like `create_package(package_type)`                 | Reduces duplication, easier to maintain, cleaner code             |
# | The `assign_type` parameter name is unclear (`packages`)    | Rename parameter to `quantity`                                               | Makes code more intuitive and self-explanatory                    |
# | Returning a list of lists                                   | Return a dictionary `{ "normal": [...], "express": [...], "urgent": [...] }` | Easier to manipulate, avoids index confusion                      |
# | No validation for invalid package types                     | Add `else: print("Invalid type")`                                            | Prevents silent errors and improves user feedback                 |
# | `packages_count_type()` returns unclear list like `[3,1,4]` | Return a dictionary `{ "normal": 3, "express": 1, "urgent": 4 }`             | More descriptive, avoids confusion                                |
# | Repeated creation of package_info dict in each branch       | Move creation into a helper function                                         | Eliminates code repetition and consolidates logic                 |
# | Too many responsibilities inside assign_type()              | Split logic into smaller functions                                           | Code becomes easier to test, read, and scale                      |
# | Using `time.time()` repeatedly for IDs                      | Consider simple incrementing ID or UUID                                      | Prevents IDs from being almost identical and improves consistency |
# | Not using a loop variable properly (`package` unused)       | Replace `package` with `_`                                                   | Indicates intentionally unused variable, improves clarity         |
# | No stripping or normalization for input                     | Use `.strip().lower()`                                                       | Avoids errors due to accidental spaces or capitalization          |
