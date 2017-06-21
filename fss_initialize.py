import fss
import numpy

def ClientInitialize(numBits):
    f = fss
    f.NumBits = numBits
    for i in range(0, 4, 1):
        f.PrfKeys[i] = numpy.random.randint(256, size=16)
        # 以下註解是go語言 還沒改成python
        # // 產生加密用的block
        # block, err: = aes.NewCipher(f.PrfKeys[i])
        # if err != nil {
        # panic(err.Error())
        # }
        # f.FixedBlocks[i] = block

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

        # 以下註解是go語言 還沒改成python
        # // 產生加密用的block
        # block, err: = aes.NewCipher(f.PrfKeys[i])
        # if err != nil {
        # panic(err.Error())
        # }
        # f.FixedBlocks[i] = block
    # Check if int is 32 or 64 bit
    x = numpy.uint64(1 << 32)
    if numpy.uint(x) == 0:
        f.N = 32
    else:
        f.N = 64
    f.M = 4
    return f

# 測試function功能是否pass
a = ClientInitialize(4)
print(a.PrfKeys)
b = ServerInitialize(a.PrfKeys, 4)
print(b.PrfKeys)