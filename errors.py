# the errors example


# Python uses exceptions instead of the error type used in Go. 
# as such, the example is executed a bit different but the goal is 
# to show similar features

def f1(arg):
    if arg == 42:
        raise ValueError("can't work with 42")
    
    return arg + 3

def main():

    for i in [7, 42]:
        try:
            print("f1 worked:", f1(i))
        except ValueError as err:
            print("f1 failed:", err)

main()