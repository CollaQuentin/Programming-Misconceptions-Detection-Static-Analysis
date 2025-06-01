def remove(self) :
    first = self.first()
    if first is not None :
        self.__head = first.next()
        first.set_next(None)
