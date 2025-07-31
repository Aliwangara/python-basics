from django.template.defaultfilters import upper

unit = upper(input("Is this temp in celcius or Fahrenheit? (C/F)"))
temp = float(input("Enter Temp: "))

if unit == "C":
    temp = round((temp*9)  /5 +32 ,1)
    print(f"the temperature is {temp}°Fahrenheit")
elif unit == "F":
    temp = round((temp-32)*5/9 ,1 )
    print(f"the temperature is {temp}°Celcius")

else:
    print(f"{unit} is not a valid unit")