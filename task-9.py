from helpers import input_quantity_info, ID_generator, input_string, input_number

def regiter_rooms(rooms):
    total_rooms = []
    for room in range(rooms):
        room_info = { 
            "ID": ID_generator(),
            "room_number": input_number("room number"),
            "freedom_room": input_string("if the room is freedom: s/n"),
        }
        total_rooms.append(room_info)
    return total_rooms

print(regiter_rooms(input_quantity_info("rooms")))