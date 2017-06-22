import numpy
import fss as f
import fss_util
import binary
from Crypto.Cipher import AES


class FssKeyEq2P:
    SInit = numpy.zeros((1, 16), int)
    TInit = 0
    CW = numpy.zeros((4, 16), int)
    FinalCW = 0


def GenerateTreePF(a, b):
    fssKeys = []
    for i in range(0, 2, 1):
        fssKey = FssKeyEq2P()
        fssKeys.append(fssKey)

    # 17 = AES block size + 1
    tempRand1 = numpy.random.randint(256, size=AES.block_size+1)
    print(tempRand1)
    fssKeys[0].SInit = tempRand1[0:16]
    fssKeys[0].TInit = tempRand1[16] % 2
    print(fssKeys[0].SInit)
    print(fssKeys[0].TInit)

    fssKeys[1].SInit = numpy.random.randint(256, size=AES.block_size)
    fssKeys[1].TInit = fssKeys[0].TInit ^ 1

    print(fssKeys[1].SInit)
    print(fssKeys[1].TInit)

    sCurr0 = fssKeys[0].SInit
    sCurr1 = fssKeys[1].SInit
    tCurr0 = fssKeys[0].TInit
    tCurr1 = fssKeys[1].TInit

    leftStart = 0
    rightStart = AES.block_size + 1

    for i in range(0, 6, 1):
        fss_util.prf(sCurr0, f.FixedBlocks, 3, f.Temp, f.Out)
        prfOut0 = f.Out[0:48]
        fss_util.prf(sCurr1, f.FixedBlocks, 3, f.Temp, f.Out)
        prfOut1 = f.Out[0:48]

        t0Left = prfOut0[AES.block_size] % 2
        t0Right = prfOut0[(AES.block_size * 2) + 1] % 2
        t1Left = prfOut1[AES.block_size] % 2
        t1Right = prfOut1[(AES.block_size * 2) + 1] % 2
        # Find bit in a
        aBit = fss_util.getBit(a, (f.N - f.NumBits + i + 1), f.N)
        # Figure out which half of expanded seeds to keep and lose
        keep = rightStart
        lose = leftStart
        if aBit == 0:
            keep = leftStart
            lose = rightStart

        # Set correction words for both keys. Note: they are the same
        for j in range(0, AES.block_size, 1):
            fssKeys[0].CW[i][j] = prfOut0[lose + j] ^ prfOut1[lose + j]
            fssKeys[1].CW[i][j] = fssKeys[0].CW[i][j]

        fssKeys[0].CW[i][AES.block_size] = t0Left ^ t1Left ^ aBit ^ 1
        fssKeys[1].CW[i][AES.block_size] = fssKeys[0].CW[i][AES.block_size]
        fssKeys[0].CW[i][AES.block_size + 1] = t0Right ^ t1Right ^ aBit
        fssKeys[1].CW[i][AES.block_size + 1] = fssKeys[0].CW[i][AES.block_size + 1]

        for j in range(0, AES.block_size, 1):
            sCurr0[j] = prfOut0[keep + j] ^ (tCurr0 * fssKeys[0].CW[i][j])
            sCurr1[j] = prfOut1[keep + j] ^ (tCurr1 * fssKeys[0].CW[i][j])

        tCWKeep = fssKeys[0].CW[i][AES.block_size]
        if keep == rightStart:
            tCWKeep = fssKeys[0].CW[i][AES.block_size + 1]

        tCurr0 = (prfOut0[keep + AES.block_size] % 2) ^ tCWKeep * tCurr0
        tCurr1 = (prfOut1[keep + AES.block_size] % 2) ^ tCWKeep * tCurr1

    # Convert final CW to integer
    sFinal0, _ = binary.varint(sCurr0[:8])
    sFinal1, _ = binary.varint(sCurr1[:8])
    fssKeys[0].FinalCW = (int(b) - int(sFinal0) + int(sFinal1))
    fssKeys[1].FinalCW = fssKeys[0].FinalCW
    return fssKeys


a = GenerateTreePF(5, 1)
print(a)
