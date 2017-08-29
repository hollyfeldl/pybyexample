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

    # copy the string
    c = s
    print("cpy:", c)

    # take a slice
    l = s[2:5]
    print("sl1:", l)

    l = s[:5]
    print("sl2:", l)

    l = s[2:]
    print("sl3:", l)

    t = "ghi"
    print("dcl:", t)

    twoD = [None] * 3
    for i in range (0,3):
        innerLen = i + 1
        twoD[i] = [None] * innerLen
        for j in range (0,innerLen):
            twoD[i][j] = i + j

    print("2d: ", twoD)

main()
