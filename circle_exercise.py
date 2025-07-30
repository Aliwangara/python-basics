import  math

radius = float(input("Enter the radius of the circle: "))

total  = 2 * math.pi * radius
total = round(total,2)

print(f"The total area of the circle is: {total}cm")

area = math.pi * pow(radius, 2)

print(f"The total area of the circle is: {round(area,2)}cm")

a =float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = math.sqrt(pow(a,2) + pow(b,2))

print(f"The area is {round(c,2)}")
