# dictionary = a collection of {key : value} pairs
#              ordered and changeable. No duplicates

capitals = {
    "usa": "Washington D.C",
    "India": "New Delhi",
    "china" : "Beijing",
    "russia": "moscow"
}

print(capitals)
print(dir(capitals))
print(capitals.get("usa"))

if capitals.get("Japan"):
    print(f"capital exists")
else:
    print(f"doesn't exist")

capitals.update({"Germany": "Berlin"}) # - adds an item in the dictionary
capitals.pop("china") # -  removes an item from the dictionary
capitals.popitem() # - removes the recent item to be added in the dictionary
capitals.keys() # get key  without values
capitals.values() # get values without keys
# capitals.clear()
items = capitals.items() # returns a dictionary object which resembles a 2d list of tuples
print(items)

for key , value in capitals.items():
    print(f"{key} : {value}")