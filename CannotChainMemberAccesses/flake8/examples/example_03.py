def remove (self) :
    if self.__head is None :
        return self
    first = self.__head
    second = first.__next
    self.__head = second
    self.__length -= 1
    first.__next = None
    return self
