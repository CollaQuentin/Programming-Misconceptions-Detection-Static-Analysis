def remove(self):
    if self.__head==None:
        return
    first=self.__head
    first.next=None
    self.__head=self.__head.next()
    self.__length-=1
