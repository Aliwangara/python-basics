# collections = variable used to store multiple variables
#         list[] = ordered and changeable. Duplicate OK
#         set = {} ordered and immutable, but add/remove OK. NO duplicates
#           Tuple = () ordered and unchangeable. duplicate OK. Faster

# eg:
fruits = ["mango", "banana", "oranges", "Guava"]
fruits.insert(1, "Tomato")
fruits.append("Grapes") # pushes a new data to the end of a list
# fruits.clear()
# fruits.remove("Guava") - removes the said element

fruits.pop(3)
# fruits.sort() - sort elements in alphabetical order
# fruits.reverse() - reverses the elements in the list from last to first
# fruits.index("Guava") - gives index of the element
# fruits.count()- counts the number of time an item appears in the list
# print(fruits.copy()) Returns a copy fo the list.

print(dir(fruits))
print(help(fruits))
print(len(fruits))



# print(fruits[::-1])
for x in fruits:
    print(x)


# Set

set_fruits = {"apples", "Bananas", "Oranges", "Guava"} # a set is random and doesnt give a constant index to a value eg: print(set_fruits):
    # 1. = guava, oranges,Apples
    # 2. = oranges Bananas, Apples
#     3. = Apples,oranges


# set_fruits.remove("Guava") - removes an element
# set_fruits.add("")- adds an item to the set
# set_fruits.pop() - removes the first item in the set
# set_fruits.clear()-clears the set
# len(set_fruits) - finds the length of the set
print(dir(set_fruits))


# Tuples - faster than list

tuples_fruits = ("mango", "banana", "oranges", "Guava")





