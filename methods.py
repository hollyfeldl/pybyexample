# methods example
# ignore the component about pointers

class rect:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __repr__(self):
        # make the representation look like Go structs
        return ('{%s %s}' 
                % (repr(self.width), repr(self.height)))

    def area(self):
        """define the area of rectangle"""
        return self.width * self.height

    def perim(self):
        """define the perimeter of rectangle"""
        return (2 * self.width) + (2 * self.height)

def main():

    r = rect(10, 5)

    print("area: ", r.area())
    print("perim:", r.perim())


main()