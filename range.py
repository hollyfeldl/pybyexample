# range example 

def main():

    nums = [2, 3, 4]
    sum = 0

    for num in nums:
        sum += num

    print("sum:", sum)

    # punt on the example with index for now

    kvs = {"a": "apple", "b": "banana"}
    for k in kvs:
        print("{0:s} -> {1:s}".format(k, kvs.get(k)))

    for k in kvs:
        print("key:", k)

    # print out the unicode values for the string
    i = 0
    for c in "python":
        print(i, c, ord(c))
        i += 1

if __name__ == '__main__':
    main()