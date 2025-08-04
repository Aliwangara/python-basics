# Logical Operators = evaluate multiple conditions(or,and,not)
#                  or = atleats one condition must be true
#                   not  = inverts the condition (not False, Not True)
from django.template.defaultfilters import upper

temp = 29
is_sunny = False

if temp >=28   and is_sunny:
    print("Its Hot Outside")

elif temp >=28   and not is_sunny:
    print("Its cloudy")

else:
    print("it is Cold outside")

weather = input("What is the weather out the weather? ")
weather.capitalize()

if weather == "Cloudy":
    print("Weather is abit unredictable carry your umbrella just incase")
elif weather == "Sunny":
    print("Weather is fine for outdoor activities")
elif weather == "Rain":
    print("Dont go out today")




