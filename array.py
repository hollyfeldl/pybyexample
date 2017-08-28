# example for arrays

import numpy as np

def main():

    # create an empty list of 5 positions
    a = [None] * 5
    print("emp:", a)

    a[4] = 100
    print("set:", a)
    print("get:", a[4])

    print("len:", len(a))

    # init a list with values

    b = [1, 2, 3, 4 ,5]
    print("dcl:", b)

    # use lists for two-d array
    twoD = [ [None] * 3 ] * 2

    # use numpy to handle arrays 
    twoDNP = np.zeros((2, 3), np.int64)

    # loop over the dimensions of the arrays
    for i in range(0,2):
       for j in range(0,3):
            twoD[i][j] = i + j
            twoDNP[i][j] = i + j

    print("2d: ", twoD)
    print("2d (NP): ", twoDNP)


main()
