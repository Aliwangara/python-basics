# 🪐 Mars Mission Planner — Challenge Steps
#
# 1. Write a function to calculate how long it takes
#    to reach Mars at a given speed.
#    - Mars' average distance is 225,000,000 km.
#    - Use the formula: time = distance ÷ speed
#    - Round the result to the nearest hour.
#
# 2. Write another function to figure out the total fuel cost
#    for a mission.
#    - Formula: total cost = distance × fuel usage × price per liter
#
# 3. Test your functions with the provided mission data:
#    - Pathfinder: 40,000 km/h
#    - Perseverance: 75,000 km/h
#    - Starship: 120,000 km/h
#    - Each mission travels 225 million km,
#      burns 0.3 liters/km, and fuel costs $1.80/L.
#
# 4. For each mission, print a report showing:
#    - Mission name
#    - Travel time (hours)
#    - Total fuel cost

# Mission data
mission_1_speed = 40000  # Pathfinder
mission_2_speed = 75000  # Perseverance
mission_3_speed = 120000  # Starship

mars_distance = 225_000_000  # in kilometers
fuel_rate = 0.3  # liters per kilometer
fuel_price = 1.8  # dollars per liter


def travel_time(distance, speed):
    return round(distance / speed)


def mission_cost(distance, fuel_rate, fuel_price):
    total_fuel = distance * fuel_rate
    cost = total_fuel * fuel_price
    return cost


# Pathfinder
time_1 = travel_time(mars_distance, mission_1_speed)


# Perseverance
time_2 = travel_time(mars_distance, mission_2_speed)


# Starship
time_3 = travel_time(mars_distance, mission_3_speed)




total_cost_fuel =  mission_cost(mars_distance, fuel_rate, fuel_price)

print("===== Mars Mission Planner =====\n")
print("Mission: Pathfinder")
print("Travel time:", time_1, "hours")
print(f"Fuel cost: ${total_cost_fuel:.2f}")

print("\nMission: Perseverance")
print("Travel time:", time_2, "hours")
print(f"Fuel cost: ${total_cost_fuel:.2f}")

print("\nMission: Starship")
print("Travel time:", time_3, "hours")
print(f"Fuel cost: ${total_cost_fuel:.2f}")