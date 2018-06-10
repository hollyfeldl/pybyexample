# the structs example
# in Python let us use classes

class person:
    def __init__(self, name=None, age=0):
        self.name = name
        self.age = age
    def __repr__(self):
        # make the representation look like Go structs
        return ('{{{0} {1}}}'.format(repr(self.name), repr(self.age)))

def main():

    print(person("Bob", 20))

    print(person(name="Alice", age=30))

    print(person(name="Fred"))

    # skip pointers, show you can switch order
    print(person(age=40, name="Ann"))

    s = person(name="Sean", age=50)
    print(s.name)

    # skip the pointer fun
    print(s.age)

    # change the age directly
    s.age = 51
    print(s.age)

if __name__ == '__main__':
    main()

