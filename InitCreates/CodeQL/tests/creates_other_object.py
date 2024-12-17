class Dog:
    def __init__(self, name):
        self.name = name


class Human:
    def __init__(self, name, pet_name):
        self.name = name
        self.pet = Dog(pet_name)
