from enum import member

print("=== 🏋️ Ali's Fitness & Social Club ===\n")

try:


    name = input("Enter your name: ").strip().lower().title()
    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight: "))
    height = float(input("Enter your height: "))

    height_m = height/100
except ValueError:
    print("Invalid input! Please enter numbers for age, weight, and height.")
    exit()


bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "obese"

print(f"\n{name}, your BMI is {bmi:.2f} ({category})\n")

workouts =[]

print("Add your favourite workouts (type d or done) when you finish")

while True:
    workout = input("Workout: ").strip().lower().title()
    if workout == "done" or workout == "d":
        break
    elif workout != '':
        workouts.append(workout)
    else:
        print("Invalid input!")
member = {
    "name": name,
    "age": age,
    "weight": weight,
    "height": height,
    "bmi": round(bmi,1),
    "category":category,
    "workouts":workouts

}

event_name = input("\nEnter event name: ").strip().title()
event_date = input("Enter event date (e.g., 2025-06-15): ").strip()
event_city = input("Enter event city: ").strip().title()

event = {
    "name": event_name,
    "date": event_date,
    "city": event_city,
}

event_tuple = tuple(event.values())



