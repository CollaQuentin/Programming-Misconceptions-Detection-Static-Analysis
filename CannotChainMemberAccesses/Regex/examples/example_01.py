def remove(self) :
    first = self.first()
    first.set_next(None)
    self.head = self.first().next()
