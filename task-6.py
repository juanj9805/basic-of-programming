# MY VERSION

number_of_vehicles = int(input("How many vehicles do you want to fix: "))

def reparations_register(vehicles):
    vehicles_info = []
    for vehicle in range(vehicles):
        license_plate = input("Enter the license of the vehicle: ")
        work_hours = int(input("How many hours are neccesary: "))
        pieces_changed = int(input("How many pieces were changed: "))
        vehicle_info = {
            "license_plate":license_plate,
            "work_hours":work_hours,
            "pieces_changed":pieces_changed,
        }
        vehicles_info.append(vehicle_info)
        print("-"*30)
    return vehicles_info

def total_cost_repair(vehicles):
    hour_price = 2000
    piece_price = 5000
    total_prices = []
    for vehicle in vehicles:
        total_hour_price = vehicle["work_hours"] * hour_price
        total_piece_price = vehicle["pieces_changed"] * piece_price
        total_info_vehicle = {
            "total_hour_price":total_hour_price,
            "total_piece_price":total_piece_price,
        }
        total_prices.append(total_info_vehicle)
    return total_prices

print(total_cost_repair(reparations_register(number_of_vehicles)))

def complexity_vehicle(vehicles):
    high_complications = []
    low_complications = []
    for vehicle in vehicles:
        if vehicle["work_hours"] >10 or vehicle["pieces_changed"] > 4:
            high_complications.append(vehicle)
        else:
            low_complications.append(vehicle)
    return [high_complications,low_complications]

print(complexity_vehicle(reparations_register(number_of_vehicles)))

# CHATGPT VERSION

def reparations_register(number_of_vehicles):
    vehicles = []
    for _ in range(number_of_vehicles):
        license_plate = input("Enter the vehicle license: ")
        work_hours = int(input("How many work hours: "))
        pieces_changed = int(input("How many pieces were changed: "))
        print("-" * 30)

        vehicles.append({
            "license_plate": license_plate,
            "work_hours": work_hours,
            "pieces_changed": pieces_changed,
        })
    return vehicles


def add_costs(vehicles):
    HOUR_PRICE = 2000
    PIECE_PRICE = 5000

    for vehicle in vehicles:
        vehicle["total_hour_price"] = vehicle["work_hours"] * HOUR_PRICE
        vehicle["total_piece_price"] = vehicle["pieces_changed"] * PIECE_PRICE
        vehicle["total_cost"] = (
            vehicle["total_hour_price"] +
            vehicle["total_piece_price"]
        )
    return vehicles


def classify_complexity(vehicles):
    high = []
    low = []

    for v in vehicles:
        if v["work_hours"] > 10 or v["pieces_changed"] > 4:
            high.append(v)
        else:
            low.append(v)

    return high, low


number_of_vehicles = int(input("How many vehicles? "))

vehicles = reparations_register(number_of_vehicles)
vehicles = add_costs(vehicles)
high, low = classify_complexity(vehicles)

print("\n=== HIGH COMPLEXITY VEHICLES ===")
for v in high:
    print(v)

print("\n=== LOW COMPLEXITY VEHICLES ===")
for v in low:
    print(v)

# SUMMARY OF IMPROVEMENTS

# | **Problem**                                                       | **Fix**                                                         | **Why**                                                                          |
# | ----------------------------------------------------------------- | --------------------------------------------------------------- | -------------------------------------------------------------------------------- |
# | You call `reparations_register()` **twice**                       | Call it **once**, store the result in a variable                | Avoids asking the user for the same data twice and prevents inconsistent results |
# | Cost info is **not linked** to vehicle info                       | Add cost fields directly to each vehicle dictionary             | Keeps all data for each vehicle together, making the output meaningful           |
# | No **total cost** is calculated                                   | Add a `total_cost = hour_total + piece_total` field             | Makes the final repair cost easy to use and display                              |
# | Functions contain **print()** logic that mixes UI and computation | Remove unnecessary prints or move them outside functions        | Improves separation of concerns and keeps functions reusable                     |
# | Raw dictionaries printed without formatting                       | Format the output or loop through vehicles with readable prints | Makes results easier to understand and professional                              |
# | Variable names like `vehicles` used both as count and as a list   | Use clearer names: `number_of_vehicles`, `vehicles_list`        | Avoids confusion and improves code readability                                   |
# | Repeated constant values inside loops                             | Define constants once: `HOUR_PRICE = 2000`                      | Improves performance and avoids magic numbers                                    |
# | No validation for user input                                      | Add checks (e.g., integers, non-empty strings)                  | Prevents crashes and improves reliability                                        |
# | Calculation logic scattered                                       | Keep processing functions separate and pure                     | Cleaner code structure and easier debugging                                      |
# | `vehicle` dictionary lacks identifying keys in cost function      | Keep license plate, hours, pieces, and costs together           | Ensures consistent data across the program                                       |
