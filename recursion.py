#recursion example

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

def main():

    # compute the factoral of 7
    print(fact(7))


if __name__ == '__main__':
    main()

