# the errors example


# Python uses exceptions instead of the error type used in Go. 
# as such, the example is executed a bit different but the goal is 
# to show similar features

def f1(arg):
    if arg == 42:
        raise ValueError("can't work with 42")
    
    return arg + 3

# define a custom error

class ArgError(Exception):
    pass

def f2(arg):
    if arg == 42:
        raise ArgError("{0} - can't work with it".format(arg))

    return arg + 3

def main():

    for i in [7, 42]:
        try:
            print("f1 worked:", f1(i))
        except ValueError as err:
            print("f1 failed:", err)

    for i in [7, 42]:
        try:
            print("f2 worked:", f2(i))
        except ArgError as err:
            print("f2 failed:", err)

    # Python doesn't pass variables for errors 

if __name__ == '__main__':
    main()