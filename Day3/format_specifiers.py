#{}-format a value based on what flags are inserted.
#name = "Ali wangara"
#eg (f"my name is {name}")

price1 = 3.14657
price2 = -9764.21
price3 = 1200.343

print(f"price1 is {price1:.2f}")# makes the decimal place to be 1 eg from 3.14657 to 3.14
print(f" price2 is {price2:.1f}")# makes the decimal place to be 1 eg from -9764.21 to -9764.2
print(f"price3 is {price3:.2f}")

print(f"price1 is ${price1:10}")#adds 10 spaces before the output eg: price1 is $   3.14657

print(f"price2 is ${price2:010}")
print(f"price3 is ${price3:+,.2f}")
