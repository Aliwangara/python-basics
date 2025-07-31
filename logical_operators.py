# Logical Operators = evaluate multiple conditions(or,and,not)
#                  or = atleats one condition must be true
#                   not  = inverts the condition (not False, Not True)

temp = 29
is_sunny = False

if temp >=28   and is_sunny:
    print("Its Hot Outside")

elif temp >=28   and not is_sunny:
    print("Its cloudy")

else:
    print("it is Cold outside")


