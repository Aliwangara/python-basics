
# Exercise
# 1. Add new print statement - on a new line
#    which says 'We hear you like the color xxx! xxx is a string with color
# 2. extend the function with another  input parameter 'color', that defaults to 'red'
# 3. Capture the color via an input box as variable:color
# 4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday
#  adding 1 to the age
# 5. Capitalize first letter of the 'name', and rest are small caps
# 6. Favorite color should be in lowercase

def greeting(name, age, color='red'):
    print(f"Hello {name} you will be {age+1 }Years old next birthday")
    print(f"We Hear You like the color {color}! ")
name = input("What is your name? ").capitalize()
age = int(input("What is your age? "))
color = input("What is your favorite color? ").lower()




greeting(name, age, color)

# named notation

    # the argument doesn't have to be in the same position as the parameter you can use = to change position eg:

def person(name, height, race, age):

    print(f"hello {name} of {age} years old your race is {race} and you are {height} Tall")
person(age = 20, name = "Ali", race= "Black", height="5'8")


# return statements

def value_added_tax(amount):
    tax = amount * 0.25
    total = amount * 1.25
    return tax # returns the tax value as a float
    # return tax, total  -returns a tuple
    # return [tax, total] - returns a list
    ## return {tax, total} - returns a set
#    # return f"{tax}, {total}" - returns a string

print(value_added_tax(100))

# you can store the function name plus argument in a variable then call the variable down there eg:

price = value_added_tax(100)
print(price)






