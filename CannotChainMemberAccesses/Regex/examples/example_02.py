def remove(self):
    if self.__head is not None:
        node = self.__head
        self.__head = node.next()
        self.__length -= 1
