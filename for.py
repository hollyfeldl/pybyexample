# looping examples

def main():

    i = 1
    while i <= 3:
        print(i)
        i = i + 1

    for j in range(7,10):
        print(j)

    while True:
        print("loop")
        break

    for n in range(1,6):
        if n%2 == 0:
            continue
        print(n)

if __name__ == '__main__':
    main()
