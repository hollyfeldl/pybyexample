# the constant example

import math

s = "constant"

def main():
    print(s)

    n = 500000000

    d = 3e20 / n

    print('{:6.0e}'.format(d))

    print(d)

    print(math.sin(n))

if __name__ == '__main__':
    main()
