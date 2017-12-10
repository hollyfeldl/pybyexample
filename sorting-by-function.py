# the sort by function example

def sortFunction(x):
    return len(x)

def main():

    fruits = ["peach", "banana", "kiwi"]
    print(sorted(fruits, key=sortFunction))

if __name__ == "__main__":
    main()

