import binary
from Crypto.Cipher import AES
import FssKeyEq2P
import os
import fss_util _

def GenerateTreePF(a, b):
    fssKeys = FssKeyEq2P[2]

    tempRand1 = bytes[AES.BlockSize + 1]

    os.urandom().Read(tempRand1)

    fssKeys[0].SInit = tempRand1[:AES.BlockSize]

    fssKeys[0].TInit = tempRand1[AES.BlockSize] % 2

    fssKeys[1].SInit = bytes[AES.BlockSize]

    os.urandom().Read(fssKeys[1].SInit)

    fssKeys[1].TInit = fssKeys[0].TInit ^ 1

    sCurr0 = bytes[AES.BlockSize]
    sCurr1 = bytes[AES.BlockSize]
    copy(sCurr0, fssKeys[0].SInit)
    copy(sCurr1, fssKeys[1].SInit)
    tCurr0 = fssKeys[0].TInit
    tCurr1 = fssKeys[1].TInit

    fssKeys[0].CW = bytes[f.NumBits]
    fssKeys[1].CW = bytes[f.NumBits]
    for i = uint(0);i < f.NumBits;i + + {
        // make AES block size + 2bytes
        fssKeys[0].CW[i] = bytes[:AES.BlockSize + 2]
        fssKeys[1].CW[i] = bytes[AES.BlockSize + 2]
    }

    leftStart = 0
    rightStart = AES.BlockSize + 1

    for i = uint(0);i < f.NumBits;i + + {
        // "expand" seed into two seeds + 2 bits

    // see prf @ fss_util
    // random value array length 16, [0x.. 0x.. 0x.. 0x..], 3, Sixteen zero, Sixty four zero
    prf(sCurr0, f.FixedBlocks, 3, f.Temp, f.Out)

    prfOut0 = bytes[AES.BlockSize * 3]
    copy(prfOut0, f.Out[:AES.BlockSize * 3])

    prf(sCurr1, f.FixedBlocks, 3, f.Temp, f.Out)

    prfOut1 = bytes[AES.BlockSize * 3]
    copy(prfOut1, f.Out[:aes.BlockSize * 3])

    // fmt.Println(i, sCurr0)
    // fmt.Println(i, sCurr1)
    // Parse
    out
    "t"
    bits
    t0Left:= prfOut0[aes.BlockSize] % 2
    t0Right:= prfOut0[(aes.BlockSize * 2) + 1] % 2
    t1Left:= prfOut1[aes.BlockSize] % 2
    t1Right:= prfOut1[(aes.BlockSize * 2) + 1] % 2
              // Find
    bit in a
    aBit:= getBit(a, (f.N - f.NumBits + i + 1), f.N)

           // Figure
    out
    which
    half
    of
    expanded
    seeds
    to
    keep and lose
    keep:= rightStart
    lose:= leftStart
    if aBit == 0
    {
        keep = leftStart
    lose = rightStart
    }
    // fmt.Println("keep", keep)
       // fmt.Println("aBit", aBit)
       // Set
    correction
    words
    for both keys.Note: theyare the same
    for j: =
    0;
    j < aes.BlockSize;
    j + + {
        fssKeys[0].CW[i][j] = prfOut0[lose + j] ^ prfOut1[lose + j]
    fssKeys[1].CW[i][j] = fssKeys[0].CW[i][j]
    }
    fssKeys[0].CW[i][aes.BlockSize] = t0Left ^ t1Left ^ aBit ^ 1
    fssKeys[1].CW[i][aes.BlockSize] = fssKeys[0].CW[i][aes.BlockSize]
    fssKeys[0].CW[i][aes.BlockSize + 1] = t0Right ^ t1Right ^ aBit
    fssKeys[1].CW[i][aes.BlockSize + 1] = fssKeys[0].CW[i][aes.BlockSize + 1]

    for j: =
    0;
    j < aes.BlockSize;
    j + + {
        sCurr0[j] = prfOut0[keep + j] ^ (tCurr0 * fssKeys[0].CW[i][j])
    sCurr1[j] = prfOut1[keep + j] ^ (tCurr1 * fssKeys[0].CW[i][j])
    }
    // fmt.Println("sKeep0:", prfOut0[keep:keep + aes.BlockSize])
       // fmt.Println("sKeep1:", prfOut1[keep:keep + aes.BlockSize])
    tCWKeep:= fssKeys[0].CW[i][aes.BlockSize]
    if keep == rightStart
    {
        tCWKeep = fssKeys[0].CW[i][aes.BlockSize + 1]
    }
    tCurr0 = (prfOut0[keep + AES.BlockSize] % 2) ^ tCWKeep * tCurr0
    tCurr1 = (prfOut1[keep + AES.BlockSize] % 2) ^ tCWKeep * tCurr1
    }
    // Convert final CW to integer

    sFinal0, _= binary.Varint(sCurr0[:8])
    sFinal1, _= binary.Varint(sCurr1[:8])
    // fmt.Println("sCurr0[:8]", sCurr0[:8])
    // fmt.Println("sFinal0", sFinal0)

    // fmt.Println("sCurr1[:8]", sCurr1[:8])
    // fmt.Println("sFinal1", sFinal1)

    fssKeys[0].FinalCW = (int(b) - int(sFinal0) + int(sFinal1))
    fssKeys[1].FinalCW = fssKeys[0].FinalCW
    if tCurr1 == 1 {
    fssKeys[0].FinalCW = fssKeys[0].FinalCW * -1
    fssKeys[1].FinalCW = fssKeys[0].FinalCW
    }
    return fssKeys