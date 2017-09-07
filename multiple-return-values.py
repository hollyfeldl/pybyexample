
# the multiple return value example

def vals():
    return 3, 7


# a function that returns a tuple
def polyFacts( l, h):
    # return a tuple...
    return ((2*l)+(2*h), l*h)

def main():

    a, b = vals()
    print(a)
    print(b)

    # unlike Go, in Python you have to provide all the expected Vars
    blank, c = vals()
    print(c)

    # For a little extra fun... 
    # get the results of a tuple, comma not needed here
    (perm, area) = polyFacts( 2, 3)
    print("Tuple - Perm:", perm, "Area:", area)

    # you can still do the variable assignment the Go way if the 
    # return is a tuple
    perm, area = polyFacts( 2, 3)
    print("NoTuple - Perm:", perm, "Area:", area)

main()