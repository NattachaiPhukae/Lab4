class Length:
    def __init__(self, length):
        self.length = length

    def get(self):
        return self.length


class Width:
    def __init__(self, width):
        self.width = width

    def get(self):
        return self.width


class Height:
    def __init__(self, height):
        self.height = height

    def get(self):
        return self.height


class Pyramid:
    def __init__(self, length, width, height):
        self.length = Length(length)
        self.width = Width(width)
        self.height = Height(height)

    def volume(self):
        vol = self.length.get() * self.width.get() * self.height.get() / 3
        return round(vol, 2)

    def __repr__(self):
        return "Pyramid with length " + str(self.length.get()) + ", width "\
            + str(self.width.get()) + ", and height " + \
            str(self.height.get()) + " has volume " + str(self.volume())


p = Pyramid(10, 7, 17)
print(p)