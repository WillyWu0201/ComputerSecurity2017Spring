import sys
import binary
import numpy

initPRFLen = 4


def randomcryptoint():
    b = numpy.random.randint(sys.maxsize, size=8)
    ans, _ = binary.varint(b)
    return numpy.uint(ans)


test = randomcryptoint()
print(test)
