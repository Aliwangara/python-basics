#Compound interest calculator


principle = 0
rate = 0
time = 0

while principle <=0:
    principle = float(input("Enter your principle amount: "))

    if principle <=0:
        print("principle can't be less than or equal to zero")

while rate <=0:
   rate = float(input("Enter your interest rate: "))

   if rate <=0:
        print("rate can't be less than or equal to zero")

while time <=0:
    time = float(input("Enter your time in years: "))

    if time <=0:
        print("time can't be less than or equal to zero")

total = principle *pow ((1+rate / 100), time)

print(f"Balance after {time} year/s: ${total:,.2f} ")


