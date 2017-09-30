# if-else example

def main():

    if 7%2 == 0:
        print("7 is even")
    else:
        print("7 is odd")

    if 8%4 == 0:
        print("8 is divisible by 4")

    num = 9
    if num < 0:
        print(num, "is negative")
    elif num < 10:
        print(num, "has 1 digit")
    else:
        print(num, "has multiple digits") 

if __name__ == '__main__':
    main()
