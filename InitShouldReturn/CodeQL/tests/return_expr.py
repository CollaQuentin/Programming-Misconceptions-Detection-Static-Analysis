class Dog:
    def bark(self):
        print('Woof !')

    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
        return "Dog created"
