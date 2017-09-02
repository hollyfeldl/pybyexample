# functions example

# since there is no typing needed will just add
def plus( a, b):
	return a + b

def plusPlus( a, b, c):
    return a + b + c

# a function that returns a tuple
def polyFacts( l, h):
    return (2*l)+(2*h), l*h

def main():

    res = plus(1, 2)
    print("1+2 =", res)

    # since python doesn't care about types can also do strings
    res = plus("Pyt","hon")
    print("'Pyt'+'hon' =", res)

    # treat both sides like a tuple, need a comma on the right 
    # side so Python treats the output like a tuple
    (res,) = (plusPlus(1, 2, 3),)
    print("Tuple - 1+2+3 =", res)

    # get the results of a tuple, comma not needed hear because 
    # the output is a tuple by default
    (perm, area,) = (polyFacts( 2, 3))
    print("Tuple - Perm:", perm, "Area:", area)

    # you can do it the variable assignment the Go way as well
    perm, area = polyFacts( 2, 3)
    print("NoTuple - Perm:", perm, "Area:", area)

main()

