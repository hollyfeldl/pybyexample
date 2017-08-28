# slices example

def main():

    # make a string with three spaces
    # in Python, a string is its own sequence
    s = " " * 3
    print("emp:", s)

    s = "a" + s[1:3]
    s = s[0:1] + "b" + s[2:3]
    s = s[0:2] + "c"

    print("set:", s)
    print("get:", s[2])

    print("len:", len(s))

    s = s + "d"
    s = s + "e" + "f"

    print("apd:", s)

main()
