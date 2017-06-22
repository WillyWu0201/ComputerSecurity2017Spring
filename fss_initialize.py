import fss
import numpy

def ClientInitialize(numBits):
    f = fss
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
    f = fss
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

# 測試function功能是否pass
# a = ClientInitialize(4)
# print(a.FixedBlocks)
# b = ServerInitialize(a.PrfKeys, 4)
# print(b.FixedBlocks)