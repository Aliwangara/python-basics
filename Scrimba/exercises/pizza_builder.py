#  🍕 Pizza Builder — Challenge Steps
#
# 1. Define a Pizza class that stores:
#    - size, crust type, and a list of toppings
# 2. Add a method to add a new topping
# 3. Add a method to remove a topping if it exists
# 4. Add a method to print pizza details:
#    - size, crust, and all toppings (or “No toppings yet!”)
# 5. Create a pizza object, customize it, and print the summary



# class Pizza:
#     while True:
#
#
#         new_topping = input("Type the topping you want: ").lower().capitalize()
#         toppings = []
#
#         if new_topping in toppings:
#             toppings.pop(toppings.index(new_topping))
#         elif new_topping not in toppings:
#             toppings.append(new_topping)
#         else:
#
#             def __init__(self, size, crust_type,toppings):
#                 self.size = size
#                 self.crust_type = crust_type
#                 self.toppings = list(toppings)
#             def pizza_information(self):
#                 print("Size: ", self.size)
#                 print("Crust Type: ", self.crust_type)
#                 print("Toppings: ", self.toppings)
#
#         print(toppings)
# pizza_1 = Pizza.pizza_information()
#
# print(pizza_1)

class Pizza:
    def __init__(self, size, crust,toppings=None):
        self.size = size
        self.crust = crust
        self.toppings = toppings if toppings else []
    def add_topping(self, topping):
        self.toppings.append(topping)

    def remove_topping(self, topping):
        if topping in self.toppings:
         self.toppings.remove(topping)
        else:
            print(f'{topping} is not on your pizza')
    def describe_pizza(self):
        print("\n ==== your Pizza ==== ")

        print(f"size: {self.size.title()}")
        print(f"crust: {self.crust.title()}")
        if self.toppings:
            print(f"toppings:")
            for topping in self.toppings:
                print(f" -{topping.title()}")
            else:
                print("No toppings added Yet")

my_pizza = Pizza("large", "thin")
my_pizza.add_topping("pepperoni")
my_pizza.add_topping("mushrooms")
my_pizza.add_topping("onions")

my_pizza.describe_pizza()





