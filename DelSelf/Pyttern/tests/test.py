class Dog:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def kill(self):
        del self
