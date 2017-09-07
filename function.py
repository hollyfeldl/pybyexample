# functions example

# since there is no typing needed will just add

def plus( a, b):
	return a + b

def plusPlus( a, b, c):
    return a + b + c

def main():

    res = plus(1, 2)
    print("1+2 =", res)

    # since python doesn't care about types can also do strings
    res = plus("Pyt","hon")
    print("'Pyt'+'hon' =", res)

    # add another parm
    res = plusPlus(1, 2, 3)
    print("1+2+3 =", res)

    # treat both sides like a tuple, need a comma on the right 
    # side so Python treats the output like a tuple
    # this becomes handy with multiple return values
    (res,) = (plusPlus(1, 2, 3),)
    print("Tuple - 1+2+3 =", res)

main()

