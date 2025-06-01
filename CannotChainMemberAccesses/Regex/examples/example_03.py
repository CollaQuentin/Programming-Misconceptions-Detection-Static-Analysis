def remove():
    if self.length == 0:
        return
    first = self.first()
    self.first() = first.next()
    first = None
    self.length -= 1
