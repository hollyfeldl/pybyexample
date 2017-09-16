# interfaces example

# let's use inheritance and duck-typing 
# Python also has abstract base classes which are closer to GO
# interfaces but usage in Python is rarer

import math

class geometry:
    def __init__(self):
        pass
    def measure(self):
        print(self)
        print(self.area())
        print(self.perim())     


class rect(geometry): # inherit geometry
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    def __repr__(self):
        return ('{%s %s}'
            % (repr(self.width), repr(self.height)))
    def area(self):
        return self.width * self.height
    def perim(self):
        return 2 * (self.width + self.height)


class circle(geometry): #inherit geometry
    def __init__(self, radius=0):
        self.radius = radius
    def __repr__(self):
        return ('{%s}'
            % (repr(self.radius)))
    def area(self):
        return math.pi * self.radius * self.radius
    def perim(self):
        return 2 * math.pi * self.radius

# do the same example with abstract base classes (ABC) at a later date


def main():

    r = rect(width=3, height=4)
    c = circle(radius=5)

    r.measure()
    c.measure()

main()

