# maps example (in Python, they are Dictionaries)

def main():

    # create an empty dict
    m = {}

    # append a key-value pair to the existing dict
    # if we did m = {"k1": 7} ... we would re-init m 
    m.update({"k1": 7})
    # append a second key-value pair
    m.update({"k2": 13})

    print("map:", m)

    # get the value of a key
    v1 = m.get("k1")
    print("v1: ", v1)

    # print the current length of the dict
    print("len:", len(m))

    # delete entry by key
    del(m["k2"])

    print("map:", m)

    # check if key "k2" is in the dict
    if "k2" in m:
        print("prs:", True)
    else:
        print("prs:", False)

    # alternate using default for get
    print("prs:", m.get("k2", False))

    # define a dict in one pass
    n = {"foo": 1, "bar": 2}
    print("map:", n)

main()

