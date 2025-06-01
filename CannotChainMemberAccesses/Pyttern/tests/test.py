class Dog:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
if True:
    d = Dog("Harry")
    print(d.get_name())
