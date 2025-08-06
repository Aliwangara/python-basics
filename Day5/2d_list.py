fruit =["apples", "oranges", "banana", "coconut"]
vegetable =["celery", "carrots", "potatoes"]
meat = ["chicken", "fish", "turkey"]

fruit.insert(1,"Tomatoes")

groceries= [fruit, vegetable, meat]

print(groceries)
# to get items found in a particular list we use
print(groceries[0][1]) # = tomatoes checks the fist list and the 2nd item in the list

#iterating over

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()