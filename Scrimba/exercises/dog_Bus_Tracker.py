
max_seats = 4

bus = {
    1: {"name": "Buddy", "breed": "Golden Retriever", "pickup": "8:00 AM", "dropoff": "3:00 PM"},
    2: {"name": "Luna", "breed": "Beagle", "pickup": "8:15 AM", "dropoff": "2:45 PM"},
    3: {"name": "Max", "breed": "Bulldog", "pickup": "8:30 AM", "dropoff": "4:00 PM"}
}

print("===== STARTING ROSTER =====")

for seat,info in bus.items():
    print(f"Seat: {seat}: {info['name']} (pickup {info['pickup']})")

if len(bus) < max_seats:
    seat_num = len(bus) +1
    new_pet = {
        "name": "Sir Barks-a-Lot",
        "breed": "Corgi Knight",
        "pickup": "8:45 AM",
        "dropoff": "4:45 PM",
    }

    bus[seat_num] = new_pet
    print(f"\n👋  {new_pet['name']} boards (seat {seat_num}).")
else:
    print("\n🚫  No free seats.")


print("----- Roster After Pickup ------")

for seat,info in bus.items():
    print(f"seat: {seat}: {info['name']}")

remove_name = input("Who goes home early? ").strip().lower()
seat_to_remove = 0
for seat,info in bus.items():
    if remove_name == info['name'].lower():
        seat_to_remove+=1
        break
if seat_to_remove == 0:
    gone = bus.pop(seat_to_remove)
    print(f"\n👋  {gone['name']} (seat {seat_to_remove}) heads home early.")
else:
  print(f"\n⚠️  No passenger name '{remove_name}' on the bus.")


print("\n-- Final roster --")
for seat, info in bus.items():
  print(f"Seat {seat}: {info['name']} (drop-off {info['dropoff']})")


