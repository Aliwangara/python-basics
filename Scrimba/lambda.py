

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