

class Person:
    def __init__(self):
        print("move 4 Paces")
    def rest(self):
        print("Gain 4 points")


class Doctor(Person):
    def heal(selfs):
        print("Heal 10 health points")

class Fighter(Person):
    def fight(self):
        print("Deducts 10 health points")
    def move(self):
        print("move 6 paces")

class Wizard(Doctor):
    def cast_spell(self):
        print("Turn Invisible")


character1 = Fighter()