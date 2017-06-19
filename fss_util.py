import sys
import binary
import numpy

initPRFLen = 4


def randomcryptoint():
    #print(numpy.iinfo(numpy.int32).max)

    # the value sys.maxint, which is either 231 - 1 or 263 - 1 depending on your platform.
    #sys.maxint
    b = numpy.random.randint(numpy.iinfo(numpy.int32).max, size=8)

    #print(b)
    ans, _ = binary.varint(b)
    print(ans)
    return numpy.uint(ans)


test = randomcryptoint()
print(test)