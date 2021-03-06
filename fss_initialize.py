import fss
import numpy

class fss:
    PrfKeys = numpy.zeros((4, 16), int)
    FixedBlocks = []
    M = 0
    N = 0
    NumBits = 0
    Temp = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0]
    Out = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0]

def ClientInitialize(numBits):
    f = fss()
    f.NumBits = numBits
    for i in range(0, 4, 1):
        f.PrfKeys[i] = numpy.random.randint(256, size=16)
        # 產生加密用的block
        f.FixedBlocks.append(numpy.random.randint(999999999, size=44))
        f.FixedBlocks.append(numpy.random.randint(999999999, size=44))

    # Check if int is 32 or 64 bit
    x = numpy.uint64(1 << 32)
    if numpy.uint(x) == 0:
        f.N = 32
    else:
        f.N = 64
    f.M = 4
    return f


def ServerInitialize(prfKeys, numBits):
    f = fss()
    f.NumBits = numBits
    for i in range(0, 4, 1):
        f.PrfKeys[i] = prfKeys[i]
        # 產生加密用的block
        f.FixedBlocks.append(numpy.random.randint(999999999, size=44))
        f.FixedBlocks.append(numpy.random.randint(999999999, size=44))

    # Check if int is 32 or 64 bit
    x = numpy.uint64(1 << 32)
    if numpy.uint(x) == 0:
        f.N = 32
    else:
        f.N = 64
    f.M = 4
    return f
