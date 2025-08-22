
#  a class is a blueprint or a representation of something that is about to be created.
#  an object is now the representation or the thing that has been created from the class.

# variables - attribuites
# functions - methods


# class naming we use CamelCase eg:
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def car_information(self):
        print("Car Brand:", self.make)
        print("Model:", self.model)
        print("Year:", self.year)
car_1 = Car("Toyota", "Harrier", 2022)
car_2 = Car("Subaru", "N10", 2010)

car_1.car_information()
