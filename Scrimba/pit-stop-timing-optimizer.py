# 🏁 Pit Stop Timing Optimizer 🔧
#
# 1. Ask the user for the total race time in seconds.
# 2. Ask how many pit stops were made.
# 3. Ask for the average pit stop duration (in seconds).
#
# Then:
# - Calculate the total pit stop time.
# - Calculate the percentage of the race spent in the pits.
# - Round the percentage to 2 decimal places.
#
# Finally, print all of the following:
# - Total pit stop time in seconds
# - Percentage of race time spent in pits
# - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️"


race_time = float(input("Enter the total race time in seconds(S): "))
pits_made = int(input("Enter the number of pits made: "))
pits_stop_duration = float(input("Enter the average pit stop duration in seconds(S): "))

total_pit_stop_time = pits_made * pits_stop_duration

time_spent_in_pits = (total_pit_stop_time/race_time) *100

round(time_spent_in_pits, 2)

print(total_pit_stop_time)
print(f"Total time spent in pits is: {time_spent_in_pits:>10}%")

if time_spent_in_pits > 5:
    print("You need a new pit crew. 🛠️")
