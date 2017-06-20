import binary
import numpy
from Crypto.Cipher import AES
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


def prf(x,aesBlocks,numBlocks, temp, out ):
    #If request blocks greater than actual needed blocks, grow output array

    # initPRFLen 4

    if numBlocks > initPRFLen :
        #out = make([]byte, numBlocks*aes.BlockSize)
        f = []

        for i in range(numBlocks*AES.block_size):
            f.append(0)
        print(f)

    for i in range(numBlocks):
        # get AES_k[i](x)
        aesBlocks[i].Encrypt(temp, x)   #still go

        # get AES_k[i](x) ^ x
        for j in range(temp):
            out[i * AES.block_size + j] = temp[j] ^ x[j]

prf(2,0,5,3,3)