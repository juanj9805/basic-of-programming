import time

def input_quantity_info(info_type):
    quantity = int(input(f"How many {info_type} do you want to register: "))
    return quantity

def ID_generator():
    id = time.time()
    return id

def input_string(name):
    name =  input(f"Register the {name}: ")
    return name

# def input_quantity_each_item():
#     quantity =  int(input("Product quantity: "))
#     return quantity

def input_number(value):
    price =  int(input(f"Register the {value}: "))
    return price