# the closure example

def intSeq():
    i = 0

    def Seq():
        # use the nonlocal keyword so that we 
        # can modify i
        nonlocal i
        i += 1
        return i

    # since Seq() is a nested function
    # that operates on a value of the enclosing function
    # we can return Seq as the closure
    return Seq

def main():

    nextInt = intSeq()

    print(nextInt())
    print(nextInt())
    print(nextInt())

    newInts = intSeq()

    print(newInts())

main()    