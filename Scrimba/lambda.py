

# This is the normal function
def square(x):
    return x*x
print(square(5))

# but with lambda instead of doing that we can use

# variable = lambda x (which is the name of the expression) : x*x which is the operation to be performed
# print(variable(5)) gives 25

square1 = lambda x : x*x
print(square1(5))

# we can use multiple expressions and syntax in lambda eg:

triangle = lambda  b,h: (1/2*b)*h

print(triangle(5,2))

# third eg:

name_and_alias = lambda name,alias : name + ":" + alias

print(name_and_alias("John","Doe"))




monty_python = ['John Marwood Cleese','Eric Idle','Michael Edward Palin','Terrence Vance Gilliam','Terry Graham Perry Jones', 'Graham Arthur Chapman']

monty_python.sort(key=lambda name:name.split(' ')[::-1])
print(monty_python)
# monty_python.sort(key= sort_names)
print(monty_python)

def func(n):
    return lambda a : a*n

print(type(func(1)))
doubler = func(2)
print(doubler(3))
quintipler = func(5)
print(quintipler(3))
print(type(func(3)))

def add(b):
    return lambda a : a+b

number1 = add(2)
lam = add(3)
print(lam)


def price_calc(start,hourly_rate):
    return lambda hours: start + hourly_rate * hours

walking_cost = price_calc(10,30)
premium_cost = price_calc(1,25)
print(walking_cost(2))
print(premium_cost(2))