from array import *


def productOfArray(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * productOfArray(arr[1:])


res = productOfArray(array('i', [2, 4, 3, 6]))
print(res)
