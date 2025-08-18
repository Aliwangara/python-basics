

max_seats = 4

bus = {
    1: {"name": "Buddy", "breed": "Golden Retriever", "pickup": "8:00 AM", "dropoff": "3:00 PM"},
    2: {"name": "Luna", "breed": "Beagle", "pickup": "8:15 AM", "dropoff": "2:45 PM"},
    3: {"name": "Max", "breed": "Bulldog", "pickup": "8:30 AM", "dropoff": "4:00 PM"}
}

for key,value in bus.items():
    if max_seats<=len(bus):
        print(key, value)
    else:
        print("The bus is full")

