#Strings

name =  "Ali"

#integers

age = 20

#floats

weight = 54.7

# boolean
is_married = True

# to check data type we use type() eg

print(type(name))

#Type casting
#if we use print(name + age) = error.  So in this case we use typecasting eg:
print(name  +  str(age)) # = Ali 20

# other forms of typecasting are

a = int(1)# = 1
b = int(2.5) #= 2
c= int("3") # = 3
# c1 = int("3.4")   # c1 will be error unless you cast it into a float first then to an integer eg int(float("3.4))
d = float(1)      # d will be 1.0
e = float(2.5)    # e will be 2.5
f = float("3")    # f will be 3.0
g = float("4.23") # g will be 4.23
h = str("80s")    # h will be '80s'
i = str(22)       # i will be '22'
j = str(3.01)     # j will be '3.01'

#Create appropriate Variables for Item name, the price
#and how many you have in stock

item_name = "macbook"
price = 20000
quantity = 100

print(item_name, price, quantity)
