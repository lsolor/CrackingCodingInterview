import math
import sys


def smallestDifference(arrA, arrB):
    ptrA = 0
    ptrB = 0
    minDiff = abs(arrA[ptrA]-arrB[ptrB])

    #loop while both are in bounds
    while((ptrA < len(arrA)) and (ptrB <len(arrB))):

        #Get difference if we advance ptrA
        if(ptrA + 1 < len(arrA)):
            diffA = abs(arrA[ptrA+1] - arrB[ptrB])
        else:
            diffA = sys.maxsize

        #Get difference if we advance ptrB
        if(ptrB + 1< len(arrB)):
            diffB = abs(arrB[ptrB+1] - arrB[ptrB])
        else:
            diffB = sys.maxsize

        if(diffB == sys.maxsize and diffA == sys.maxsize):
            break

        #advancing pointer, if it has a lesser value
        if(diffB > diffA):
            ptrA += 1
        else:
            ptrB += 1

        #check to see if we found a lesser minDiff
        if(minDiff> abs(arrA[ptrA] - arrB[ptrB])):
            minDiff = abs(arrA[ptrA] - arrB[ptrB])

    return minDiff







if __name__ == '__main__':


    arrA = [1, 2, 3, 11, 15]
    arrB = [8, 19, 23, 127, 235]

    print(smallestDifference(arrA,arrB))