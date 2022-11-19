class Linklist:
    def __init__(self, val):
        self.val = val
        self.next = None

    def addBack(self, data):
        if self.next is None:
            self.next = Linklist(data)
        else:
            self.next.addBack(data)

    def addFront(self, data):
        temp = Linklist(data)
        temp.next = self
        return temp

    def removeIndex(self, index):
        if index == 0:
            return self.next
        else:
            self.next = self.next.removeIndex(index - 1)
            return self

    def __repr__(self):
        if self.next is None:
            return str(self.val)
        else:
            return str(self.val) + " -> " + str(self.next)


l = Linklist(44)
l.addBack(36)
l.addBack(90)
l.addBack(10)
l.addBack(60)
l.addBack(99)
print(l)
l = l.addFront(104)
print(l)
l.addBack(57)
print(l)
l = l.removeIndex(4)
print(l)