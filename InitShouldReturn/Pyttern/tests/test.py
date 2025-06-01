class Dog:
    def __init__(self, name, legs):
        self.name = name
        print(name)
        self.legs = legs
        return Dog(name, legs)

    def get_name(self):
            return self.name
