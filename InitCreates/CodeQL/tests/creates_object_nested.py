class Dog:
    def __init__(self, name):
        self.name = name
        if name.endswith("new"):
            if len(name) == 3:
                dog = Dog(name)

