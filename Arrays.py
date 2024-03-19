import numpy


def arrays(arr):
    array_float = numpy.array(arr, float)
    return numpy.flip(array_float)


arr = input().strip().split(" ")
result = arrays(arr)
print(result)
