class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        vol = 3.1415926535 * self.radius * self.radius * self.height
        return round(vol, 2)

    def __repr__(self):
        return "Cylinder with radius " + str(self.radius) + " and height " + str(self.height) + " has volume " + str(self.volume())


c1 = Cylinder(5, 10)
c2 = Cylinder(7, 13)
print(c1)
print(c2)