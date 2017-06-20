import sys
import binary
import numpy

initPRFLen = 4


def randomcryptoint():

    # the value sys.maxint, which is either 231 - 1 or 263 - 1 depending on your platform.
    # 查看原始function，他的亂數都小於256
    b = numpy.random.randint(256, size=8)

    ans, _ = binary.varint(b)
    print(ans)
    return numpy.uint(ans)

def getBit(n, N, pos):
    val = (n & (1 << (N - pos)))
    if val > 0:
        return 1
    else:
        return 0
